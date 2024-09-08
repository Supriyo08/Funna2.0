## Animal Health Monitoring and Diagnostics System

**Website Live Demo Link:** https://funna-care.vercel.app/ 

#### Abstract

Our system provides a comprehensive and user-friendly method for monitoring and diagnosing animal health issues. By continuously tracking vital signs like heart rate, blood oxygen levels, and temperature, we reduce veterinary costs and prevent serious disorders through early detection and treatment. Accessibility is ensured via an IVR system, a website, and a mobile app. Real-time telehealth integration enables instant veterinary consultations during emergencies, improving overall animal health.

#### Keywords:

- Animal healthcare
- Explainable AI (artificial intelligence)
- Image classification (disease detection)
- IoT (Internet of Things)

#### System Description:

- Continuously monitors vital signs through wearable IoT sensors.
- Provides user-friendly interfaces for mobile app, website, and IVR for accessibility.
- Integrates real-time telehealth for immediate veterinary consultations.
- Utilizes machine learning models for:
- Identifying animal species in images.
- Filtering noise from sensor data for accurate diagnoses.


#### Main Outcomes:

- Continuous monitoring of vital signs.
- Accessible via multiple platforms (mobile app, website, IVR).
- Real-time telehealth consultations.
- Machine learning for disease detection and animal identification.

#### Data:

- Parameters: Heart rate, blood oxygen, temperature, species classification, disease detection, user access metrics, telehealth logs.
- Sources: IoT sensors, digital images, user interactions, telehealth service logs.


#### Methodology:

**1.Data Collection:** Monitors vital signs and gathers images.
**2.Machine Learning:**
**3.Identifies animal** species in images.
**4.Detects diseases** from images.
**5.Analyzes sensor** data (e.g., ECG) for abnormalities.
**6.Telehealth Integration:** Enables real-time consultations with veterinarians.


#### Components:

**1.IoT Device:** Wears on the animal to track vital signs.
**2.Web Interface:** Provides access to system functionalities on a computer.
**3.Mobile App:** Offers a user-friendly platform for smartphones.
**4.Datasets:** Collections of data for training machine learning models (e.g., animal images, ECG recordings).
**5.Machine Learning Models:** Algorithms for specific tasks (e.g., image classification, disease detection, ECG analysis).
**6.Convolutional Neural Networks (CNN)** and **EfficientNetB0** for image classification.
**7.Random Forest** for disease detection.
**8.Gradient Descent** for ECG analysis.
**9.Telehealth Features:** Provides video calls and chat functionality for consultations.

![Screenshot 2024-06-29 131312](https://github.com/supriyo010/funna-care/assets/130129570/a9264b24-1e54-4871-bc7e-78024e1fd2d4)



#### Accuracy and Results:

- ECG Analysis: 86% accuracy.
- Lumpy Skin Cancer Detection: 89% accuracy.
- Image Classification: Over 80% accuracy.


#### Validation Strategy:

- Data Validation: Ensures data quality through cleaning and verification.
- Model Validation: Uses cross-validation techniques to assess model performance.
- Telehealth Validation: Simulates consultations and gathers user feedback for improvement.
