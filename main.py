from transformers import LlamaForCausalLM, LlamaTokenizer

# Define the path to your model directory.
model_dir = "your_model_url"  #You can download the binary file (fine-tuned) from HuggingFace, if you want

# Load the model and tokenizer.
model = LlamaForCausalLM.from_pretrained(model_dir)
tokenizer = LlamaTokenizer.from_pretrained(model_dir)

# If you want to run your model on the GPU, specify the device.
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Generate text with the model.
input_text = "Your input text here."
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
output = model.generate(input_ids, max_length=100, num_return_sequences=3, no_repeat_ngram_size=2)

# Decode and print the generated text.
for i, sequence in enumerate(output):
    generated_text = tokenizer.decode(sequence, skip_special_tokens=True)
    print(f"Generated text {i+1}: {generated_text}")
