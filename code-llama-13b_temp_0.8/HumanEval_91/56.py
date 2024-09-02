
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
    if len(S) < 2:
        return 0
    punctuation = ['.', '?', '!']
    count = 0
    s = S.lower()
    for x in punctuation:
        s = s.replace(x, ' ' + x)
    for word in s.split():
        if word[0] == 'i':
            count += 1
    return count
