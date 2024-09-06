
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
    if S:
        word_count = 0
        prev_word = ''
        for w in S:
            if w == 'I':
                if prev_word and prev_word != 'I':
                    word_count += 1
            elif w == '.':
                if word_count > 0:
                    word_count -= 1
                    prev_word = ''
            elif w == '?':
                if word_count > 0:
                    word_count -= 1
                    prev_word = ''
                elif word_count == 0 and prev_word == 'I':
                    word_count += 1
            elif w == '!':
                if word_count > 0:
                    word_count -= 1
                if word_count == 0 and prev_word == 'I':
                    return 1
            prev_word = w
        return word_count