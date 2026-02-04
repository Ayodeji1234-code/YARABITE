<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yarabite Kitchen - Delicious Home-Style Meals</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #f5f5dc; /* Soft cream for cleanliness */
            color: #a0522d; /* Warm brown */
        }
        .navbar {
            background-color: #8b0000; /* Deep red */
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .navbar-brand {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            color: #ffd700 !important; /* Gold */
        }
        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://via.placeholder.com/1920x1080/228b22/ffffff?text=Jollof+Rice+with+Chicken') no-repeat center center;
            background-size: cover;
            height: 80vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }
        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .btn-primary {
            background-color: #ffd700; /* Gold */
            border-color: #ffd700;
            color: #8b0000;
            font-weight: 700;
        }
        .btn-primary:hover {
            background-color: #a0522d; /* Warm brown */
            border-color: #a0522d;
        }
        .section {
            padding: 4rem 0;
        }
        .menu-item {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            overflow: hidden;
        }
        .menu-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .menu-item h5 {
            color: #8b0000;
            font-family: 'Playfair Display', serif;
        }
        .footer {
            background-color: #a0522d;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        .footer a {
            color: #ffd700;
            text-decoration: none;
        }
        .footer a:hover {
            color: white;
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="#">Yarabite Kitchen</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#menu">Menu</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <h1>Welcome to Yarabite Kitchen</h1>
            <p class="lead">Delicious home-style and restaurant-quality meals with a modern Nigerian/continental touch. Fresh, hygienic, and mouth-watering.</p>
            <a href="#menu" class="btn btn-primary btn-lg">Explore Our Menu</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h2>About Us</h2>
                    <p>Yarabite Kitchen brings you the best of Nigerian flavors with a continental twist. Our meals are prepared with fresh ingredients, ensuring quality and hygiene in every bite. Perfect for young adults and families seeking premium yet affordable dining.</p>
                    <p>Emphasizing warmth, trust, and delicious presentation, we make every meal feel like home.</p>
                </div>
                <div class="col-md-6">
                    <img src="https://via.placeholder.com/600x400/228b22/ffffff?text=Fresh+Ingredients" alt="Fresh Ingredients" class="img-fluid rounded">
                </div>
            </div>
        </div>
    </section>

    <!-- Menu Section -->
    <section id="menu" class="section bg-light">
        <div class="container">
            <h2 class="text-center mb-4">Our Menu</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="menu-item">
                        <img src="https://via.placeholder.com/400x300/8b0000/ffffff?text=Jollof+Rice" alt="Jollof Rice">
                        <div class="p-3">
                            <h5>Jollof Rice with Grilled Chicken</h5>
                            <p>Rich, spicy rice with tender chicken, fresh peppers, and aromatic spices.</p>
                            <p class="text-muted">$15.99</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="menu-item">
                        <img src="https://via.placeholder.com/400x300/a0522d/ffffff?text=Egusi+Soup" alt="Egusi Soup">
                        <div class="p-3">
                            <h5>Egusi Soup with Pounded Yam</h5>
                            <p>Traditional Nigerian soup with melon seeds, meats, and fluffy pounded yam.</p>
                            <p class="text-muted">$12.99</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="menu-item">
                        <img src="https://via.placeholder.com/400x300/228b22/ffffff?text=Grilled+Fish" alt="Grilled Fish">
                        <div class="p-3">
                            <h5>Grilled Fish with Vegetable Medley</h5>
                            <p>Fresh fish grilled to perfection with a continental vegetable side.</p>
                            <p class="text-muted">$18.99</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2 class="text-center mb-4">Contact Us</h2>
            <div class="row">
                <div class="col-md-6">
                    <form>
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input type="text" class="form-control" id="name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email</label>
                            <input type="email" class="form-control" id="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="message" class="form-label">Message</label>
                            <textarea class="form-control" id="message" rows="4" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Send Message</button>
                    </form>
                </div>
                <div class="col-md-6">
                    <p><strong>Address:</strong> 123 Flavor Street, Lagos, Nigeria</p>
                    <p><strong>Phone:</strong> +234 123 456 7890</p>
                    <p><strong>Email:</strong> info@yarabitekitchen.com</p>
                    <p>Follow us on social media for mouth-watering updates!</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Yarabite Kitchen. All rights reserved.</p>
            <p>Follow us: <a href="#">Instagram</a> | <a href="#">Facebook</a> | <a href="#">Twitter</a></p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Simple form submission alert (for demo purposes)
        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your message! We\'ll get back to you soon.');
        });
    </script>
</body>
</html>