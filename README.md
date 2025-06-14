# Best Crop Recommendation System

# Live on [RENDER](https://best-crop-recommendation-system.onrender.com)

![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Introduction
The **Best Crop Recommendation System** is a web-based application designed to recommend the best crop to plant based on soil conditions, weather, and other environmental factors. This project uses machine learning to analyze input data and provide accurate and data-driven recommendations to farmers and agricultural enthusiasts.

## Project Structure
```
project/
├── app.py
├── templates/
│   ├── index.html
│   ├── result.html
│   └── nav.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   ├── rice.jpg
│   │   └── placeholder.jpg
├── xgboost_model.pkl
└── label_encoder.pkl
```
## Features
- User-friendly interface for data input and results.
- Predicts the best crop to plant based on environmental factors.
- Includes navigation to home, about, and contact pages.
- Provides detailed insights about recommended crops.

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/best-crop-recommendation.git
   ```

2. Navigate to the project directory:
   ```bash
   cd best-crop-recommendation
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:
   ```bash
   flask run
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Access the homepage of the application.
2. Navigate to the "Form" section to input soil and environmental data.
3. Submit the form to receive crop recommendations.
4. Explore the "About" and "Contact" pages for more information about the project.

## Technologies Used
- **Python**: Backend development using Flask.
- **HTML/CSS**: Frontend design and structure.
- **Machine Learning**: Crop recommendation model using XGBoost.
- **JavaScript**: Interactive components.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

## Acknowledgments
- Inspired by the need for sustainable agriculture solutions.
- Special thanks to open-source contributors and libraries.

---

Feel free to report issues or suggest features in the [issues section](https://github.com/SameerAha-007/best-crop-recommendation/issues).

