
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
    result = 0
    current_sentence = []
    for word in S.split():
        if word in ['.', '?', '!']:
            if current_sentence[0] == 'I':
                result += 1
            current_sentence = []
        else:
            current_sentence.append(word)
    return result

