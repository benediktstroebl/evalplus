
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
    # We'll use a dictionary to store the count of words that start with "I"
    count = {}
    
    # Iterate through the words
    for word in S:
        # If the word starts with "I", add it to the count dictionary
        if word.startswith("I"):
            count[word] = count.get(word, 0) + 1
    
    return max(count.values())
