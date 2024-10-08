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
    bored_count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if sentence:
            first_word = sentence.split()[0]
            if first_word == 'I':
                bored_count += 1
        questions = sentence.split('?')
        for question in questions:
            if question:
                first_word = question.split()[0]
                if first_word == 'I':
                    bored_count += 1
        exclamations = sentence.split('!')
        for exclamation in exclamations:
            if exclamation:
                first_word = exclamation.split()[0]
                if first_word == 'I':
                    bored_count += 1
    return bored_count
