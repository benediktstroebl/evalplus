def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = S.split(".")
    sentences = [sent.strip() for sent in sentences]
    sentences = [sent for sent in sentences if len(sent) > 0]
    sentences += S.split("?")
    sentences = [sent.strip() for sent in sentences]
    sentences = [sent for sent in sentences if len(sent) > 0]
    sentences += S.split("!")
    sentences = [sent.strip() for sent in sentences]
    sentences = [sent for sent in sentences if len(sent) > 0]
    
    boredom_count = 0
    for sent in sentences:
        if sent.startswith("I"):
            boredom_count += 1
            
    return boredom_count
