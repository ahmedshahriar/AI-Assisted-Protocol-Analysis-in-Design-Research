def calculate_openai_cost(usage, prompt_cost_per_1000, completion_cost_per_1000):
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens
    
    prompt_cost = (prompt_tokens / 1000) * prompt_cost_per_1000
    completion_cost = (completion_tokens / 1000) * completion_cost_per_1000
    
    total_cost = prompt_cost + completion_cost
    return total_cost, prompt_tokens, completion_tokens, total_tokens
    

