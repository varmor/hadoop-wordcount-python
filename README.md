# Word Count using Hadoop MapReduce with Python (Streaming on Dataproc)

This project explores the **core concepts of distributed data processing** using the  **MapReduce programming model** , implemented with **Python** via  **Hadoop Streaming** , and deployed on a multi-node **Google Cloud Dataproc** cluster.

### 🎯 Purpose

The goal of this project was to gain hands-on experience with large-scale data processing in a distributed cloud environment using industry-standard tools. Rather than using Java for MapReduce (the traditional approach), this project leverages **Hadoop Streaming** to execute custom **Python scripts** for the map and reduce phases making it more accessible for data engineers and Python practitioners.

### 🛠 Key Features

* ✅ **MapReduce-based Word Count** implementation
* ✅ Executed on a **multi-node Dataproc cluster** with production-like configuration
* ✅ Uses **HDFS** for input/output data storage
* ✅ Mapper and Reducer implemented in **Python**
* ✅ Demonstrates full **Map → Shuffle & Sort → Reduce** pipeline
* ✅ Integrates **Python + Hadoop** via **Streaming API**
* ✅ Cloud-native setup using **Google Cloud Platform (GCP)**

---

## 📦 Project Structure

```bash
wordcount_project/
├── data
|└── input.txt
├── mapper.py
└── reducer.py
```

---

## 🔧 Prerequisites

- A working Hadoop environment, either:
  - **Locally** set up on your system (with HDFS and MapReduce configured), or
  - **Cloud-based**, e.g. a Google Cloud **Dataproc** cluster with Hadoop installed
- Python 3 installed on all nodes (local machine or cluster)
- Hadoop Streaming JAR available(commonly found at: `/usr/lib/hadoop/hadoop-streaming-3.3.6.jar`)
- Executable permissions for both scripts:
  ```bash
  chmod +x wordcount_project/mapper.py wordcount_project/reducer.py

  ```

---

## 🧰 Cluster Setup (Google Cloud Dataproc)

- **Cluster Name:** `cluster-name`
- **Nodes:** 1 master, 2 worker nodes
- **Hadoop Version:** 3.3.x (Streaming enabled)
- **OS Environment:** Debian/Ubuntu-based Dataproc VM

### 🔐 Accessing the Cluster

You can SSH into the Dataproc master node using either of the following methods:

**Option 1: Via Google Cloud Console (Web UI)**

1. Go to the [Dataproc Clusters page](https://console.cloud.google.com/dataproc/clusters)
2. Click on your cluster: `cluster-name`
3. Select **"VM Instances"** and click **"SSH"** next to the **master node** to open a terminal in the browser

**Option 2: Via gcloud CLI**

```bash
gcloud compute ssh <your-username>@<cluster-name>-m --zone=<your-zone>
```

---

## 🚀 How to Run the Job

1. Upload Input File to HDFS

```bash
hdfs dfs -mkdir -p /user/morevarun4004/wordcount_input
hdfs dfs -put wordcount_project/data/input.txt /user/morevarun4004/wordcount_input
```

2. Ensure Mapper and Reducer Scripts Are Present Locally
   Make sure mapper.py and reducer.py are in your current working directory or provide the correct relative paths.
3. Run Hadoop Streaming Job

```bash
hadoop jar /usr/lib/hadoop/hadoop-streaming-3.3.6.jar \
  -input /user/morevarun4004/wordcount_input \
  -output /user/morevarun4004/wordcount_output \
  -mapper wordcount_project/mapper.py \
  -reducer wordcount_project/reducer.py \
  -file wordcount_project/mapper.py \
  -file wordcount_project/reducer.py 
```

4. View the Output

```bash
hdfs dfs -cat /user/morevarun4004/wordcount_output/part-0000*
```

---

### ✅ Sample Output

For the input:

```bash
hello world
hello hadoop
map reduce world
```

Expected output:

```bash
hadoop  1
hello   2
map     1
reduce  1
world   2
```

---

## 📚 Learnings

- Understood the MapReduce lifecycle (Map → Shuffle & Sort → Reduce)
- Learned how to use Hadoop Streaming to run Python scripts
- Gained experience with Google Cloud Dataproc and cluster-based HDFS storage
- Built confidence in deploying distributed data jobs in a cloud environment
