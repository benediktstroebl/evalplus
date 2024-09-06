
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
    def filter_words(S):
        """
        Filter out boredoms
        """
        return [word for word in S.split(' ')[1:] if word]
    
    def count_boredoms(S):
        """
        Count the number of boredoms
        """
        return len(filter_words(S))
    return count_boredoms(S)
