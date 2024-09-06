
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
    def scan(s):
        result = 0
        index = 0
        while index < len(s):
            if s[index] == 'I':
                result += 1
            elif s[index] == '.':
                index += 1
                if s[index] == '?':
                    index += 1
                elif s[index] == '!':
                    index += 1
            else:
                index += 1
        return result
    return scan(S)