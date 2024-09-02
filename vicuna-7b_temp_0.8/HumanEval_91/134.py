
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
    sliced_sentences = [sentence[1:].strip() for sentence in S.split(".?!")]
    return sum([len(sentence) for sentence in sliced_sentences if len(sentence)>0 and sentence[0]=='I'])
