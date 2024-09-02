
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
    def repl(m):
        """
        Replace the match object with a pair of values (match start, match end)
        """
        return (m.start(), m.end())

    def group_boredom(m):
        """
        Return the group of the boredom sentence or None if there's no boredom
        sentence
        """
        if not m.group(1):
            return None
        else:
            return m.group(0)

    def boredoms(tokens):
        """
        Find all boredom sentences in the list of tokens
        """
        boredoms = []
        for i, token in enumerate(tokens):
            if token.lower() == 'i':
                start = i
                end = tokens.index(token, i)
                boredoms.append((start, end))
        return boredoms

    def count_boredoms(tokens):
        """
        Count the number of boredoms in the list of tokens
        """
        return len(boredoms(tokens))

    s = S.strip().lower()
    boredoms = boredoms(s.split())
    return count_boredoms(s) + boredoms
