# OAAA - Face Recognition Project
[![Python](https://img.shields.io/badge/python-100%25-blue.svg)](https://www.python.org/)  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Omar-Waleeed/Face_Recognition)




Welcome to the OAAA Face Recognition Project! This application leverages `customtkinter`, `OpenCV`, and `face_recognition` libraries to create a secure sign-in and sign-up system using facial recognition technology.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Preview](#preview)

## Features

- **User Registration**: New users can sign up by entering their details and capturing their facial image.
- **User Login**: Registered users can sign in using their facial recognition.
- **User Information Display**: View registered user details.
- **Dark/Light Mode**: Toggle between dark and light mode for better user experience.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/oaaa-face-recognition.git
    cd oaaa-face-recognition
    ```

2. **Install the required packages**:
    ```bash
    pip install customtkinter opencv-python-headless face_recognition pillow
    ```

3. **Prepare the environment**:
    - Ensure you have a `data.json` file in the root directory with the following structure:
    ```json
    {
        "Accounts": []
    }
    ```
    - Place your images and icon files in the `Materials` directory:
        - `Logo-dark.ico`
        - `Background_dark.png`
        - `Background_light.png`
        - `Logo-dark.png`
        - `Logo-light.png`
        - `ieeelogo-light.png`
        - `ieeelogo-dark.png`

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Sign Up**:
    - Click on the 'Sign Up Now!' button.
    - Fill in your details and click on 'Capture Face!' to register.

3. **Sign In**:
    - Click on the 'Sign in' button.
    - Enter your username and click on 'Capture Face!' to log in.

4. **Toggle Mode**:
    - Use the 'Switch Mode' toggle to switch between dark and light modes.

## File Structure
```│
├── Accounts # Directory for storing user facial images
├── Materials # Directory for storing images and icons
│ ├── Background_dark.png
│ ├── Background_light.png
│ ├── Logo-dark.ico
│ ├── Logo-dark.png
│ ├── Logo-light.png
│ ├── ieeelogo-light.png
│ └── ieeelogo-dark.png
├── data.json # JSON file for storing user account information
├── app.py # Main application file
├── README.md # This readme file
└── requirements.txt # Required Python packages
```

## Preview
<div align="center"> 
  <img src="/Screenshots/1.png" alt="screenshot1" />
  <img src="/Screenshots/2.png" alt="screenshot2" />
  <img src="/Screenshots/3.png" alt="screenshot3" />
  <img src="/Screenshots/4.png" alt="screenshot4" />
</div>
