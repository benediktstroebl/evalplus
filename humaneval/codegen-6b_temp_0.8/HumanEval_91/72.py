
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
    def is_bored_helper(s):
        if len(s) > 0 and s[0] == "I":
            return True
        else:
            return is_bored_helper(s[1:])
    return is_bored_helper(S)
