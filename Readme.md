# Readme

### Install python, pip

### Install transformer, Pytorch
```shell
pip install transformers
pip install torch torchvision torchaudio
```
See more here: https://huggingface.co/docs/transformers/installation

### Get pretrained model from Hugging Hub
At root workspace, run script (only one time):
```shell
python get_pretrained_model.py
```

### Install flask
```shell
pip install -U Flask
```


### Run code
```shell
python ./server.py 
```


### Example
```shell
POST / HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Content-Length: 395

# Body
{
    "text": [
        "Grammarly’s plagiarism checker can detect plagiarism from billions of web pages as well as from ProQuest’s academic databases. Our free plagiarism check will tell you whether or not your text contains duplicate content. Our Premium plagiarism check highlights passages that require citations and gives you the resources you need to properly credit your sources."
    ]
}

# Response
{
    "result": [
        "The plagiarism checker from GRAMMARLY can identify plagiarism from both web pages and academic databases such as ProQuest. Our free version can reveal duplicate content in your text. Alternatively, our Premium version will highlight citation-required passages and provide ample resources for proper crediting sources.",
    
        "With the help of Grammarly, you can discover whether your text contains plagiarism from various sources, including web pages and academic databases. Our free plagiarism checker will tell you if there are duplicated content in your writing while our Premium plagiarismchecker shows you relevant passages that require citations.",
    
        "Our plagiarism checker from Grace will identify plagiarism from web pages and academic databases, as well as ProQuest ones. We offer a free one-liner that can tell you if your text contains duplicate content or an additional Premium one line that highlights passages that require citations and provides the resources to properly credit your sources.",
    
        "By using Grammarly, you can detect plagiarism on web pages and academic databases like ProQuest. Our free plagiarism checker can help you identify duplicate content in your text. Alternatively, our Premium plagiarismchecker will provide you with information on required citations and resources for proper crediting your sources without any additional checks.",
    
        "Gravity's plagiarism checker can identify plagiarism from both academic and web databases, including ProQuest. Our free plagiarism checking service can help you determine if your writing contains duplicate content. Additionally, our Premium plagiarism checks will highlight citation-required passage or even suggest relevant cited material to help with your source credit."
    ]
}
```