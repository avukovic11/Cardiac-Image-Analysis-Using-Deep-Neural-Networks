# Cardiac Image Analysis Using Deep Neural Networks

This repository contains the code and accompanying thesis for the Bachelor's project **"Analysis of Cardiac Images Using Deep Neural Networks"** by **Adam Vuković**, completed at the **Faculty of Electrical Engineering and Computing, University of Zagreb**, in June 2024.  
**Mentor:** Academician Prof. Dr. Sven Lončarić

---

## 📖 Project Overview

The project explores the application of **deep learning techniques** for the analysis of **X-ray phase contrast imaging (X-PCI)** scans of heart biopsy samples from heart transplant patients.  
The goal is to automatically detect and classify the **degree of cardiac transplant rejection**, categorized by the **International Society for Heart and Lung Transplantation (ISHLT)** into four grades: **0R, 1R, 2R, and 3R**.

Traditional manual histological analysis is time-consuming and subjective.  
This work aims to improve diagnostic accuracy and efficiency by leveraging modern **convolutional neural network (CNN)** architectures.

---

## 🧠 Methods

Two deep CNN architectures were implemented and compared:

- **ResNet-18**
- **DenseNet-121**

Both models were used for:

- **Classification tasks** (predicting discrete rejection grades)
- **Regression tasks** (predicting continuous rejection scores)

The models were implemented in **Python** using **PyTorch**, with **transfer learning** applied from ImageNet-pretrained networks.

---

## 🧩 Dataset

The dataset consists of grayscale **X-PCI images** of cardiac biopsies collected at **KBC Zagreb**.  
Images are organized into directories corresponding to the four rejection grades (**0R–3R**).  
Three datasets were created:

- **Training set:** 9 hearts  
- **Validation set:** 4 hearts  
- **Test set:** 14 hearts  

Each set contains several thousand images.  
Training and validation samples were formalin-prepared (high contrast), while test samples were not, introducing real-world variation in image quality.

---

## ⚙️ Implementation Details

- **Framework:** PyTorch  
- **Optimizer:** Adam (learning rate = 1e-5)  
- **Loss functions:**  
  - Mean Squared Error (for regression)  
  - Cross Entropy Loss (for classification)  
- **Training:** 15 epochs, mini-batch size = 4  
- **GPU acceleration via CUDA**

**Grad-CAM visualization** was used to analyze activation maps and interpret model decisions.

---

## 📊 Results

| Model | Validation Accuracy | Test Accuracy |
|:------|:--------------------:|:--------------:|
| ResNet (Regression) | 92.29% | 56.08% |
| ResNet (Classification) | 68.23% | 39.81% |
| DenseNet (Regression) | 82.89% | 50.55% |
| DenseNet (Classification) | 58.90% | 40.28% |

### Key Findings

- Regression models outperformed classification models.  
- ResNet achieved slightly better results than DenseNet.  
- Lower test accuracy is attributed to differences in image contrast and quality between datasets.  
- Grad-CAM visualizations confirmed that regression models better localized medically relevant features.

---

## 🧭 Conclusion

Deep neural networks show strong potential for assisting in the **automated assessment of cardiac transplant biopsies**.  
Although regression-based approaches achieved promising accuracy, the study highlights the need for:

- Larger and more diverse datasets  
- Better domain-specific pretraining  
- Further optimization for medical imaging conditions

---

## 📂 Repository Contents

- `code/` – Python source code (PyTorch implementation)  
- `paper/` – Full thesis PDF  
- `README.md` – Project overview (this file)

---

## 🧑‍💻 Author

**Adam Vuković**  
Faculty of Electrical Engineering and Computing, University of Zagreb  
June 2024
