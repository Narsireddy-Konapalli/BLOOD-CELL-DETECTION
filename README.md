# Blood Cell Detection using YOLO 

This project uses a YOLO (You Only Look Once) model to detect and classify Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets in images. The interface is built with Streamlit, providing users the ability to upload an image for detection. The project is deployed on Hugging Face Spaces for easy access.

## Installation

To set up and run the project locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Narsireddy-Konapalli/blood-cell-detection.git
    cd blood-cell-detection
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. After running the Streamlit app, navigate to the provided local URL (usually `http://localhost:8501`).
2. Upload an image containing blood cells (e.g., from a microscope).
3. The app will display the uploaded image with bounding boxes drawn around detected Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets, with labels for each detected cell type.

## How It Works

- The YOLO model is pre-trained to detect blood cells in images.
- The Streamlit app serves as the user interface, allowing users to upload images.
- When an image is uploaded, it is passed through the YOLO model, which identifies and classifies RBCs, WBCs, and Platelets.
- The app outputs the image with bounding boxes around detected cells and labels them with the corresponding cell type.

## Deployment

The project is also deployed on Hugging Face Spaces, enabling easy access and usage:

[Blood Cell Detection on Hugging Face Spaces](https://huggingface.co/spaces/narsireddy/BloodAnalyzer)

## Interface

The app interface allows users to:

- Upload an image of a blood sample.
- Detect and classify Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets.
- View the image with bounding boxes and labels indicating the detected cells.

Example interface look:

![Image](https://github.com/user-attachments/assets/f3b0d44d-c0a6-4657-97ab-0e9908cacf24)

## Acknowledgments

- **YOLO (You Only Look Once)** for object detection.
- **Streamlit** for creating the web app interface.
- **Hugging Face** for hosting the deployment.
- **OpenCV** for image processing and model training.
