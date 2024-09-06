import string
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    punctuations = set(string.punctuation)
    count = 0
    for sentence in S.split(' '):
        # Trim spaces and punctuations from the sentence end
        sentence = sentence.strip('.,?!').rstrip(punctuations)
        if sentence and sentence[0] == 'I':
            count += 1
    return count