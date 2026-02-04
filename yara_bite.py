import streamlit as st
import uuid
import urllib.parse
from datetime import datetime

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Yarabite Kitchen - Delicious Meals",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for warm, appetizing design (deep reds, warm browns, greens, gold accents)
st.markdown("""
<style>
    body {
        background-color: #f5f5dc; /* Soft cream for cleanliness */
        font-family: 'Montserrat', sans-serif;
    }
    .stButton button {
        background-color: #8b0000; /* Deep red */
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #a0522d; /* Warm brown */
    }
    .stTextInput, .stTextArea, .stNumberInput {
        border-radius: 8px;
        border: 2px solid #228b22; /* Green for freshness */
    }
    .gold-accent {
        color: #ffd700; /* Gold */
        font-weight: bold;
    }
    .menu-item {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        margin-left: 20px; /* Indent items under category headers for better alignment */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 5px solid #ffd700; /* Gold accent */
    }
    .total-section {
        background-color: #a0522d;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem 0.8rem;
        }
        button {
            width: 100%;
            font-size: 16px !important;
            padding: 14px !important;
            border-radius: 10px;
        }
        input, textarea, select {
            font-size: 16px !important;
        }
        .menu-item {
            margin-left: 0; /* Remove indent on mobile for better fit */
        }
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# CONSTANTS
# ===============================
ADMIN_PASSWORD = "yarabite123"  # Updated for branding
KITCHEN_WHATSAPP = "2348169123431"  # Replace with actual number

ACCOUNT_DETAILS = {
    "bank": "Opay",
    "account_name": "Yarabite Kitchen Services",
    "account_number": "8169123431",  # Updated for branding
}

# Expanded menu with Nigerian/continental items, descriptions for appetizing appeal
MENU_ITEMS = [
    {"category": "Main Dishes", "items": [
        {"name": "Jollof Rice (Small)", "price": 200, "desc": "Spicy, aromatic rice with fresh tomatoes and peppers—restaurant-quality comfort.", "image": "https://via.placeholder.com/150x100/8b0000/ffffff?text=Jollof+Rice"},
        {"name": "Jollof Rice (Large)", "price": 500, "desc": "Generous portion of our signature dish, perfect for sharing.", "image": "https://via.placeholder.com/150x100/8b0000/ffffff?text=Jollof+Rice"},
        {"name": "Fried Rice (Small)", "price": 200, "desc": "Fluffy rice stir-fried with veggies and a continental twist.", "image": "https://via.placeholder.com/150x100/a0522d/ffffff?text=Fried+Rice"},
        {"name": "Fried Rice (Large)", "price": 500, "desc": "Hearty serving with fresh ingredients for ultimate satisfaction.", "image": "https://via.placeholder.com/150x100/a0522d/ffffff?text=Fried+Rice"},
        {"name": "Grilled Chicken Piece", "price": 1000, "desc": "Tender, juicy chicken grilled with herbs—premium and hygienic.", "image": "https://via.placeholder.com/150x100/228b22/ffffff?text=Chicken"},
        {"name": "Beef Stew Portion", "price": 300, "desc": "Slow-cooked beef in rich, deep red sauce with fresh spices.", "image": "https://via.placeholder.com/150x100/8b0000/ffffff?text=Beef"},
        {"name": "Egg (Boiled/Fried)", "price": 300, "desc": "Farm-fresh eggs, prepared to perfection.", "image": "https://via.placeholder.com/150x100/ffd700/000000?text=Egg"},
        {"name": "Egusi Soup with Pounded Yam", "price": 800, "desc": "Traditional Nigerian soup with melon seeds and fluffy yam—mouth-watering authenticity.", "image": "https://via.placeholder.com/150x100/228b22/ffffff?text=Egusi+Soup"},
    ]},
    {"category": "Snacks", "items": [
        {"name": "Meat Pie", "price": 500, "desc": "Crispy pastry filled with seasoned meat—perfect for a quick bite.", "image": "https://via.placeholder.com/150x100/a0522d/ffffff?text=Meat+Pie"},
        {"name": "Chicken Pie", "price": 700, "desc": "Flaky pie with tender chicken and veggies.", "image": "https://via.placeholder.com/150x100/228b22/ffffff?text=Chicken+Pie"},
        {"name": "Sausage Roll", "price": 500, "desc": "Golden, savory roll with fresh sausage.", "image": "https://via.placeholder.com/150x100/ffd700/000000?text=Sausage+Roll"},
        {"name": "Shawarma Wrap", "price": 4000, "desc": "Grilled meat in a soft wrap with veggies—continental delight.", "image": "https://via.placeholder.com/150x100/8b0000/ffffff?text=Shawarma"},
    ]}
]

# ===============================
# SESSION STATE
# ===============================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = {}

# ===============================
# HELPERS
# ===============================
def naira(x):
    return f"₦{x:,.0f}"

def cart_total():
    return sum(i["price"] * i["qty"] for i in st.session_state.cart)

def add_to_cart(name, price):
    for item in st.session_state.cart:
        if item["name"] == name:
            item["qty"] += 1
            return
    st.session_state.cart.append({"name": name, "price": price, "qty": 1})

def clear_cart():
    st.session_state.cart = []

def whatsapp_kitchen(order):
    msg = f"""
🍽️ NEW ORDER from Yarabite Kitchen

ID: {order['id']}
Name: {order['customer']}
Phone: {order['phone']}
Address: {order['address']}
Total: ₦{order['total']:,}

Items: {', '.join([f"{i['name']} x{i['qty']}" for i in order['items']])}
"""
    return f"https://wa.me/{KITCHEN_WHATSAPP}?text={urllib.parse.quote(msg)}"

def whatsapp_customer(order):
    msg = f"""
Hello {order['customer']} 👋

Your order from Yarabite Kitchen has been CONFIRMED ✅

Payment Details:
Bank: {ACCOUNT_DETAILS['bank']}
Account Name: {ACCOUNT_DETAILS['account_name']}
Account Number: {ACCOUNT_DETAILS['account_number']}
Amount: ₦{order['total']:,}

Order ID: {order['id']}
Fresh ingredients, hygienic prep—enjoy your meal!
"""
    phone = order["phone"].replace(" ", "")
    if phone.startswith("0"):
        phone = "234" + phone[1:]
    return f"https://wa.me/{phone}?text={urllib.parse.quote(msg)}"

# ===============================
# NAVIGATION
# ===============================
page = st.sidebar.radio(
    "Menu",
    ["🛒 Order", "📦 Order Status", "🔐 Admin"]
)

st.caption("☰ Open menu (top-left) to navigate | Fresh ingredients daily for quality and hygiene.")

# ===============================
# ORDER PAGE
# ===============================
if page == "🛒 Order":
    st.title("🍽️ Yarabite Kitchen")
    st.markdown("*Delicious home-style and restaurant-quality meals with a modern Nigerian/continental touch.*")

    st.subheader("Our Menu")
    for cat in MENU_ITEMS:
        st.markdown(f"### {cat['category']}")
        for item in cat["items"]:
            st.markdown('<div class="menu-item">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(item["image"], width=100)  # Appetizing image
            with col2:
                # Sub-columns for inline layout: text on left, button on right
                text_col, button_col = st.columns([3, 1])
                with text_col:
                    st.markdown(f"**{item['name']}** — {naira(item['price'])}")
                    st.caption(item["desc"])  # Mouth-watering description
                with button_col:
                    st.button("➕ Add", key=item["name"],
                              on_click=add_to_cart,
                              args=(item["name"], item["price"]))
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧾 Your Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty. Add some delicious items!")
    else:
        for item in st.session_state.cart:
            item["qty"] = st.number_input(
                f"{item['name']} (₦{item['price']} each)", 0, 20, item["qty"], key=f"qty_{item['name']}"
            )

        st.markdown('<div class="total-section">', unsafe_allow_html=True)
        st.markdown(f"### Total: {naira(cart_total())}")
        st.button("🗑️ Clear Cart", on_click=clear_cart)
        st.markdown('</div>', unsafe_allow_html=True)

        with st.form("order_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            address = st.text_area("Delivery Address")
            submit = st.form_submit_button("Place Order", help="We'll confirm via WhatsApp for hygiene and quality assurance.")

            if submit:
                if not name or not phone or not address:
                    st.error("Please fill all fields for a smooth delivery.")
                elif cart_total() == 0:
                    st.error("Your cart is empty!")
                else:
                    oid = str(uuid.uuid4())[:8].upper()
                    order = {
                        "id": oid,
                        "customer": name,
                        "phone": phone,
                        "address": address,
                        "items": st.session_state.cart.copy(),
                        "total": cart_total(),
                        "status": "Pending Review",
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.orders[oid] = order
                    st.session_state.cart.clear()

                    st.success(f"Order placed successfully! Your ID is: {oid}")
                    st.link_button("📲 Send Order to Kitchen", whatsapp_kitchen(order))

# ===============================
# ORDER STATUS
# ===============================
elif page == "📦 Order Status":
    st.title("📦 Order Status")
    st.markdown("*Track your Yarabite Kitchen order for fresh, on-time delivery.*")

    oid = st.text_input("Enter Your Order ID")
    if st.button("Check Status"):
        order = st.session_state.orders.get(oid.upper())
        if not order:
            st.error("Order not found. Double-check your ID.")
        else:
            st.success(f"Status: {order['status']}")
            st.markdown(f"**Total:** {naira(order['total'])} | **Placed:** {order['time']}")
            if order["status"] == "Confirmed":
                st.markdown("### Payment Details")
                st.write(ACCOUNT_DETAILS)
                st.info("Pay promptly for hygienic, fresh delivery.")

# ===============================
# ADMIN PANEL
# ===============================
elif page == "🔐 Admin":
    st.title("🔐 Admin Panel - Yarabite Kitchen")
    pwd = st.text_input("Enter Admin Password", type="password")

    if pwd != ADMIN_PASSWORD:
        st.warning("Access restricted to admins only.")
        st.stop()

    st.subheader("Manage Orders")
    for order in st.session_state.orders.values():
        with st.expander(f"Order {order['id']} — {order['status']} ({order['time']})"):
            st.write(f"**Customer:** {order['customer']} | **Phone:** {order['phone']} | **Address:** {order['address']}")
            st.write(f"**Items:** {', '.join([f'{i["name"]} x{i["qty"]}' for i in order['items']])}")
            st.write(f"**Total:** {naira(order['total'])}")

            status = st.selectbox(
                "Update Status",
                ["Pending Review", "Confirmed", "Completed", "Rejected"],
                index=["Pending Review", "Confirmed", "Completed", "Rejected"].index(order["status"]),
                key=order["id"]
            )

            if st.button("Update Status", key=f"up_{order['id']}"):
                order["status"] = status
                st.success("Status updated successfully!")

                if status == "Confirmed":
                    st.link_button(
                        "📲 Send Payment Details to Customer",
                        whatsapp_customer(order)
                    )