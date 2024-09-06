
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
    def word_index(s):
        index = 0
        for char in s:
            if char == 'I':
                return index
            index += 1
        return index + 1
    
    def is_boredom(s):
        for word in s.split():
            if word.startswith("I"):
                return True
        return False
    
    num_boredoms = 0
    for word in S.split():
        if is_boredom(word):
            num_boredoms += word_index(word)
    return num_boredoms
