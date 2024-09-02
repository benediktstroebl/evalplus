
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
    def is_boredom(word):
        return word[0] == "I"
    
    def is_sentence(sentence):
        return '.', '?' or '!' in sentence
    
    return sum([1 for word in S if is_boredom(word) and is_sentence(word)])