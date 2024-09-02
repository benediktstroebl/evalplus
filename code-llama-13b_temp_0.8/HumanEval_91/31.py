
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
    list_of_strings = S.split(".")
    list_of_strings1 = S.split("!")
    list_of_strings2 = S.split("?")
    print(list_of_strings)
    print(list_of_strings1)
    print(list_of_strings2)
    list_of_strings.extend(list_of_strings1)
    list_of_strings.extend(list_of_strings2)
    print(list_of_strings)
    count = 0
    for item in list_of_strings:
        if item.find("I") != -1:
            count += 1
    return count

