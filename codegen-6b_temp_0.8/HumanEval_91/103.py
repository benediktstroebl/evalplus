
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
    
    list_words = S.split(" ")
    
    len_sentence = len(list_words)
    words = []
    
    for word in list_words:
        if word.find("I") != -1:
            words.append(word[1:])
    
    return len(words)


