
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
    count = 0
    for word in S.split():
        if word.lower() == "i":
            count += 1
    return count

print(is_bored("Python"))  # 0
print(is_bored("I love Python"))  # 1
print(is_bored("Python is awesome"))  # 0
print(is_bored("Python rocks"))  # 0