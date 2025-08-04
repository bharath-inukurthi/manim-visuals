# 📚 Teaching Methods Research: Traditional vs Visual (Manim-based) Techniques

This repository was created as part of an academic research project comparing **traditional chalk-and-board teaching methods** with **visual teaching techniques** using the **Manim** animation engine. The project aims to evaluate how visualizations, especially those developed using Python-based animation libraries, can impact students’ understanding, engagement, and retention—specifically in technical subjects like deep learning.

## 🎯 Purpose

This research is focused on:
- Evaluating the effectiveness of **Manim-based visual teaching** compared to traditional methods.
- Conducting student surveys and statistical hypothesis tests on understanding, engagement, and recall.
- Generating animated educational content using Manim for specific topics.
- Measuring learning outcomes through structured experiments.

## 🧠 What is Manim?

**Manim (Mathematical Animation Engine)** is an open-source Python library for creating precise, programmatically-generated mathematical animations. It allows educators and researchers to visually represent complex mathematical and computational ideas with clarity.

Manim was originally created by **Grant Sanderson**, the creator of the popular YouTube channel **[3Blue1Brown](https://www.3blue1brown.com/)**, which is renowned for its beautifully animated explanations of math concepts.

- 🔗 **GitHub (Community Edition):** [https://github.com/ManimCommunity/manim](https://github.com/ManimCommunity/manim)
- 📺 **3Blue1Brown YouTube Channel:** [https://www.youtube.com/c/3blue1brown](https://www.youtube.com/c/3blue1brown)

## 🎥 Visual Content in this Repository

This repository includes:
- A **video explanation of forward propagation** in a simple **Multilayer Perceptron (MLP)** using Manim animations.
- The **corresponding Python script** used to generate the animation with the Manim engine.


## 🛠️ How to Run the Script

### 📦 Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/bharath-inukurthi/manim-visuals.git
cd manim-visuals
pip install -r requirements.txt
```

> Make sure you have Python 3.8+ and `ffmpeg` installed and available in your system path.

### ▶️ Rendering the Animation

To render the `ForwardPropagationDemo` scene from the Manim script:

#### High Quality (Preview + 60fps + 4K):

```bash
manim -pqk manime.py ForwardPropagationDemo
```

#### Low Quality (Faster Preview):

```bash
manim -pql manime.py ForwardPropagationDemo
```

- `-p`: Automatically preview after rendering  
- `-qk`: High-quality (4K, 60fps)  
- `-ql`: Low-quality (fast render)  

The output video will be saved in the `media/` directory.

