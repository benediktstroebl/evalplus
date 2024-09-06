
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

    from itertools import groupby
    import math

    words = sentence.split(' ')

    primes = set()
    for n in range(2, 101):
        is_prime = True
        for number in range(2, int(math.sqrt(n)) + 1):
            if n % number == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(n)

    primes = list(primes)
    primes.sort()

    for key, group in groupby(words, lambda word: len(word)):
        if key in primes:
            yield ''.join(group)
