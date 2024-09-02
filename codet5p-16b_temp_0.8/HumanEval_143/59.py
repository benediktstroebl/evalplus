
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    from itertools import takewhile
    import math
    from string import punctuation

    sentence = sentence.replace(' ', '').strip(punctuation)
    lengths = []
    for word in sentence.split():
        num_primes = sum(1 for i in range(2, int(math.sqrt(len(word))) + 1) if len(word) % i == 0)
        if num_primes == len(word):
            lengths.append(len(word))
    return''.join(takewhile(lambda x: x in lengths, sentence.split()))

