def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    num_boredoms = 0
    for sentence in S.split('. ') + S.split('? ') + S.split('! '):
        if sentence.startswith('I'):
            num_boredoms += 1
    return num_boredoms