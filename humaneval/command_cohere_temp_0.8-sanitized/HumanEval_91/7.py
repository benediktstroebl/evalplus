def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    num_boredoms = 0
    current_boredom = False
    for word in S.split():
        if word == 'I':
            current_boredom = True
        elif word in ['.', '?', '!'] :
            if current_boredom :
                num_boredoms += 1
            current_boredom = False
    return num_boredoms