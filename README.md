# AI-Assisted Protocol Analysis in Design Research

This repository contains the code and documentation for the paper "**Towards AI-Assisted Protocol Analysis in Design Research: Automating Question Labeling with GPT-4 According to Eris' (2004) Taxonomy.**"

Presented at the [DCC 2024, the 11th International Conference on Design Computing and Cognition, Montreal, Canada. 8–10 July 2024](https://sites.google.com/view/dcc24/).

## Getting Started

Create a python virtual environment and install the required dependencies -
```
pip insrall -r requirements.txt
```

Update `.env` with your settings. You can use `.env.example` as a reference:

- `OPENAI_API_KEY=<your-key>`: Your OpenAI API key.
- `OPENAI_MODEL=gpt-4-1106-preview`: GPT model version.
- `PROMPT_COST_PER_1000=0.01`: Cost for 1,000 prompt tokens in USD.
- `COMPLETION_COST_PER_1000=0.03`: Cost for 1,000 completion tokens in USD.
- `DATA_DIR=dataset`: Dataset directory.
- `DATA_FILE=convo-qs-eris-labelled.xlsx`: Your dataset. A sample dataset is available in the `dataset` folder.

Update the [system message](https://platform.openai.com/docs/guides/chat-completions/message-roles) for the OpenAI [Chat Completion API](https://platform.openai.com/docs/api-reference/chat/create) in the `system-message.txt` file.

## Experiments

The `experiments` folder contains Jupyter notebooks detailing the experiments conducted for the paper.

1. Determine the baseline performance by classifying a test set of standalone question utterances, with/without training set.
2. Determine the effect of the size of the training set on the accuracy of labelling by the GPT-4. 
3. Determine the sensitivity of the results across multiple “runs” of the experiment.
4. Determine whether the GPT-4 can also use context in the labelling task, and if it improves the labelling performance.


## Findings
- Training set could be useful
-  Labelling is probabilistic; a larger training set reduces uncertainty.
- Providing context surrounding each question results in degraded performance which aligns with recent findings on LLMs’ struggle with long context
    - One notable study by Liu et al. (2024) [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638). Transactions of the Association for Computational Linguistics, 12:157–173.
    
