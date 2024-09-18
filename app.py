from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name)

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.json
    input_text = data.get("input_text", "")
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=50)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
