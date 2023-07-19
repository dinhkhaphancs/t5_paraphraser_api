from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# run only one time
tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

# store to resuse
tokenizer.save_pretrained("./pretrain/humarin/chatgpt_paraphraser_on_T5_base")
model.save_pretrained("./pretrain/humarin/chatgpt_paraphraser_on_T5_base")