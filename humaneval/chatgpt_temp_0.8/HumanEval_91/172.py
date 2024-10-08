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
    boredom_count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if '?' in sentence:
            sub_sentences = sentence.split('?')
            for sub_sentence in sub_sentences:
                if '!' in sub_sentence:
                    mini_sub_sentences = sub_sentence.split('!')
                    for mini_sub_sentence in mini_sub_sentences:
                        if mini_sub_sentence.strip().startswith('I'):
                            boredom_count += 1
                elif sub_sentence.strip().startswith('I'):
                    boredom_count += 1
        elif '!' in sentence:
            sub_sentences = sentence.split('!')
            for sub_sentence in sub_sentences:
                if '?' in sub_sentence:
                    mini_sub_sentences = sub_sentence.split('?')
                    for mini_sub_sentence in mini_sub_sentences:
                        if mini_sub_sentence.strip().startswith('I'):
                            boredom_count +=
