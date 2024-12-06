# Portal Frame Modeling

## Description

Welcome to the **Portal Frame Modeling** repository! This project provides resources and exercises for creating a 3D CAD model of a steel portal frame structure. You will use the Open CASCADE Technology (OCC) library in Python to complete a script for generating and visualizing the portal frame model.

### **Project Overview**

In this project, you will create a parametric 3D model of a portal frame, a common structural element used in industrial buildings and warehouses. The portal frame consists of vertical columns, inclined rafters forming an "A" shape, and horizontal purlins. You will be working with existing Python scripts to complete and correct a script for generating the portal frame model.

### **Objectives**

- **Complete the  Script**: Fix errors and complete the script to generate a 3D model of a portal frame structure.
- **Create Parametric Models**: Ensure that the dimensions of the portal frame components (columns, rafters, purlins) are adjustable through parameters.
- **Visualize the Model**: Use the OCC library to visualize the final 3D model of the portal frame.

## Prerequisites

Before you start, make sure you have Python installed on your system. You will also need to install some additional packages to run the scripts and visualize the 3D model.

### Required Packages

- : The core library for working with Open CASCADE Technology in Python.
- : A set of Python bindings for Qt libraries, necessary for the OCC display functionality.

### Installation Instructions

#### Windows

1. **Install Python**:

   Download and install Python from the [official Python website](https://www.python.org/downloads/windows/).

2. **Set Up a Virtual Environment (Recommended)**:

   Open Command Prompt and create a virtual environment:

   ```bash
   python -m venv portal_frame_env
   ```

   Activate the virtual environment:

   ```bash
   portal_frame_env\Scripts\activate
   ```

3. **Install Necessary Packages**:

   Run the following commands to install the required packages:

   ```bash
   pip install pythonocc-core
   pip install PyQt5
   ```

4. **Clone the Repository**:

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/OsdagScreeningTasks/PortalFrameModeling.git
   ```

   Navigate to the project directory:

   ```bash
   cd portal_frame_modeling
   ```

5. **Run the Script**:

   Open  and run the script:

   ```bash
   python portal_frame.py
   ```

#### Linux

1. **Install Python**:

   Install Python using your package manager. For Debian-based distributions (like Ubuntu), use:

   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-pip
   ```

2. **Set Up a Virtual Environment (Recommended)**:

   Create a virtual environment:

   ```bash
   python3 -m venv portal_frame_env
   ```

   Activate the virtual environment:

   ```bash
   source portal_frame_env/bin/activate
   ```

3. **Install Necessary Packages**:

   Run the following commands to install the required packages:

   ```bash
   pip install pythonocc-core
   pip install PyQt5
   ```

4. **Clone the Repository**:

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/OsdagScreeningTasks/PortalFrameModeling.git
   ```

   Navigate to the project directory:

   ```bash
   cd portal_frame_modeling
   ```

5. **Run the Script**:

   Open  and run the script:

   ```bash
   python portal_frame.py
   ```

## Problem Statement

Your task is to complete the  script to generate a 3D model of a portal frame structure. For detailed instructions and requirements, refer to the [Problem Statement](https://github.com/your-repo/portal_frame_modeling#problem-statement) section in this repository.

### Problem Statement

In this exercise, you are required to complete the  script to create a 3D model of a steel portal frame structure. The frame should be designed to have vertical columns, inclined rafters forming an "A" shape, and horizontal purlins. 

**Tasks:**

1. **Complete the  Script**:
   - Fix errors and complete the script to correctly generate the 3D model of the portal frame structure.
   - Ensure that the frame is parametric, meaning that the dimensions of the columns, rafters, and purlins can be adjusted through parameters.
   - Include functions to create the vertical columns, inclined rafters, and horizontal purlins of the portal frame.

2. **Visualize the Model**:
   - Use the OCC library to visualize the final 3D model of the portal frame.
   - Ensure that the model accurately represents the frame's geometry and components.

**Parameters:**
- : Height of the columns
- : Thickness of the I-section columns
- : Length of the rafters
- : Thickness of the I-section rafters
- : Length of the purlins
- : Width of the purlins
- : Height of the purlins
- : Thickness of the I-section flanges
- : Thickness of the I-section web
- : Angle of inclination of the rafters (in degrees)

**Example Values**:
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

### Example Figure

For reference, you can view an example figure of the portal frame structure:

![Portal Frame Example](https://example.com/portal_frame_figure.png)

## Resources

- [**Open CASCADE Technology (OCC) Documentation**](https://www.opencascade.com/content/documentation)
- [**OCC GitHub Repository**](https://github.com/Open-Cascade-SAS/OCCT)

## Contributing

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-repo/portal_frame_modeling/blob/main/LICENSE) file for details.

## Contact

For any questions or additional information, please contact [your-email@example.com](mailto:your-email@example.com).

