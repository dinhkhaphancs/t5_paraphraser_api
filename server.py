from flask import Flask, Blueprint, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from paraphrase import paraphrase

# local model locally
device = 'cpu'
tokenizer = AutoTokenizer.from_pretrained("./pretrain/humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("./pretrain/humarin/chatgpt_paraphraser_on_T5_base").to(device)

# define routing
paraphraseRouter = Blueprint('paraphrase', __name__)
@paraphraseRouter.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return 'Paraphrase API.'

    if request.method == 'POST':
        result = paraphrase(
            tokenizer=tokenizer,
            model=model,
            question=request.json['text']
        )
        return {
            "result": result
        }


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(paraphraseRouter, url_prefix='/')
    app.run()