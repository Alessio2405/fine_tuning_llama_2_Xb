# Fine-Tune LLAMA Script

This Python script allows you to fine-tune a base machine learning model on your local machine. 
Fine-tuning is a common technique in transfer learning, where you take a pre-trained model and adapt it for a specific task or dataset. 
In this case, we'll be using the LLAMA 7B (clone) model as the base.

## Prerequisites

Before using this script, make sure you have the following installed on your local machine:

- Python (3.9 recommended)
- Required Python libraries (specified in `requirements.txt`)

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

Usage
To fine-tune the model, follow these steps:

Download Pre-trained Model: You'll need a pre-trained LLAMA model. 
You can obtain one from the official LLAMA model repository or unofficial sources (ex. HuggingFace etc.)

Prepare Your Dataset: Prepare your dataset for fine-tuning. Make sure it's organized and formatted correctly.

Configure Parameters: Adapt the parameters inside finetune_llama.py

Run the Script: Execute the script with the following command:

```bash
python finetune_llama.py
```

Monitor Progress: The script will begin fine-tuning the LLAMA model on your dataset. You can monitor the training progress in your terminal.

Evaluation and Testing: After training, you can evaluate the fine-tuned model's performance on a specific task based on your training dataset and compare it with the model before the fine-tuning.

Use the Fine-Tuned Model: Once satisfied with the fine-tuned model, you can use it for inference on new data.

Test: Download (if not running locally) .bin file that the model generated after the training phase and put it inside the main folder of the project.
Edit the variables:
-'model_dir' with the name/path of your current file
-input_text with the actual input you'd like to prompt to the model

Now run:

```bash
python main.py
```
and wait for the answer. 
Mind that using the cpu will significantly impact on model's performance.
