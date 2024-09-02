
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
    import re
    
    def count_boredoms(S):
        """
        Returns the number of boredoms in S.
        """
        boredoms = []
        for word in S.split():
            if re.search(r'\b(i?)\s.*', word):
                boredoms.append(1)
            else:
                boredoms.append(0)
        return len(boredoms)
    
    return count_boredoms(S)
