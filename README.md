
# DaVinci Resolve REST API

A **Python app** that provides a **REST API** for controlling **DaVinci Resolve** and a **Python client** to easily integrate DaVinci Resolve control into your Python applications.

This package allows users to **create, open, and manage projects**, **import media**, and **add clips to the timeline** through a **FastAPI server** and a **Python client**.

Tested with **DaVinci Resolve 18.6 (Free Version)**. It is likely compatible with newer versions as well.

Although the package is currently in its early stages with a few available endpoints, we are committed to continuously improving it and adding more functionality.

---

## **Features**

- **Create new projects** in DaVinci Resolve.
- **Open existing projects** with ease.
- **Import media clips** into the Media Pool.
- **Add clips to the timeline** with precise control.

The package includes:

- A **FastAPI server** to expose REST endpoints for DaVinci Resolve.
- A **Python client** for easy interaction from your Python applications.

---

## **Installation**

Install the package directly from **PyPI**:

```bash
pip install davinci-rest
```

> **Note:** Ensure that **DaVinci Resolve** is running and that the **FastAPI server** is started before using the client.

---

## **Starting the FastAPI Server**

The **FastAPI server** must be running to handle REST API requests.

### **Step 1: Move `launch_davinci_rest.py` to DaVinci Resolves Script Folder**

1. Navigate to DaVinci Resolves **Scripts** folder:

   - **Windows:**  
     `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\`

2. Place the `launch_davinci_rest.py` file into the **Scripts** folder.

---

### **Step 2: Run the Server from DaVinci Resolve**

Launch the server from **DaVinci Resolve**:

- Go to **Workspace -> Scripts -> launch_davinci_rest**.

Once the server is running, you can send requests to the REST API at:

```text
http://localhost:5001
```

---

## **Usage Guide**

Here is how to use the **DavinciRestClient** to interact with DaVinci Resolve via the REST API.

### **Import the Client:**

```python
from davinci_rest.client import DavinciRestClient

# Initialize the client
client = DavinciRestClient()
```

### **Example Usage:**

```python
# Create a new project
response = client.create_project("MyProject")
print(response)

# Open an existing project
response = client.open_project("MyProject")
print(response)

# Import a clip into the Media Pool
response = client.import_clip("C:\path\to\clip.mp4", "MyClip")
print(response)

# Add a clip to the timeline
response = client.add_clip_to_timeline("MyClip", start_time=10.0, duration=5.0)
print(response)
```

---

## **Available API Endpoints**

The following endpoints are exposed by the **FastAPI server**:

| **Endpoint**              | **Method** | **Description**                          |
|---------------------------|------------|------------------------------------------|
| `/project/create`          | POST       | Create a new project in DaVinci Resolve. |
| `/project/open`            | POST       | Open an existing project.                |
| `/media/import_clip`       | POST       | Import a clip into the Media Pool.       |
| `/timeline/add_clip`       | POST       | Add a clip to the timeline.              |

---

## **Want More Advanced Features?**

We are actively developing a Pro version that will include automatic subtitle generation, the ability to apply FX through the API, and more powerful endpoints for advanced control of DaVinci Resolve workflows.

Interested in the Pro version?  
Visit **[https://beluck.net/davinci-rest](https://beluck.net/davinci-rest)** to learn more and provide your feedback!

---

## **Development Status**

This package is in **early development**, and we are continuously improving the free version. Expect new features and enhancements in future updates!

We highly value user feedback. If you have suggestions or feature requests, please reach out to us!

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## **More Information**

For more information or support, please visit:

- **Website:** [https://beluck.net/davinci-rest](https://beluck.net/davinci-rest)
