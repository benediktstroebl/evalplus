
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
    words = sentence.split()
    primes = set([2, 3, 5, 7, 11, 13, 17, 19])
    # print(words)
    # print(primes)
    # print(len(primes))
    return ' '.join(filter(lambda w: len(set(w)) <= 2, words))
    # return ' '.join(filter(lambda w: len(w) in primes, words))
    # return ' '.join(filter(lambda w: len(w) in primes, words))
    # return ' '.join(w for w in words if len(w) in primes)
    # return ' '.join(w for w in words if len(set(w)) <= 2)
    # return ' '.join(w for w in words if w not in primes)

