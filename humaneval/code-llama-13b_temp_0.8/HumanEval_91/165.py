
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
    sentence_count = 0
    for i in range(len(S)):
        if S[i] == '.':
            sentence_count += 1
            if sentence_count == 2:
                break
        if S[i] == '?' or S[i] == '!':
            sentence_count += 1
            break
    return int(S.split()[0][0] == 'I') * sentence_count
