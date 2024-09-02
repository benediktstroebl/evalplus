
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
    # your code here
    sentence_delimiters = [".","?","!"]
    split_string = S.split(" ")
    list_sentences = []
    for i in range(len(split_string)):
        if(i<len(split_string)-1):
            if(split_string[i][-1] in sentence_delimiters):
                list_sentences.append(split_string[i])
        else:
            list_sentences.append(split_string[i])

    counter = 0
    for i in range(len(list_sentences)):
        if(list_sentences[i][0] == "I"):
            counter += 1

    return counter

