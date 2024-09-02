
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
    def _get_sentence(S):
        sentence = ''
        previous_word = None
        current_word = ''
        for word in S:
            if word == ' ':
                if previous_word is not None:
                    sentence += current_word
                current_word = word
            else:
                if current_word == 'I':
                    if sentence:
                        yield sentence
                    sentence = current_word
                previous_word = word
        if sentence:
            yield sentence

    def _count_boredoms(sentence):
        count = 0
        for word in sentence:
            if word == 'I':
                count += 1
        return count

    return len(_get_sentence(S))
