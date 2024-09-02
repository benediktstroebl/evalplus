
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
    def tokenize(s):
        return [word for word in s.split() if word.isalpha()]
    def is_boredom(sentence):
        return 'I' in sentence[0]
    def get_sentence_num(sentence):
        return len(sentence.split('.?!'))
    return sum([get_sentence_num(sent) for sent in tokenize(S) if is_boredom(sent)])
