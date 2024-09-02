
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
    from math import sqrt
    primes = set()
    result = []

    for n in range(2, 100):
        is_prime = True
        for m in range(2, int(sqrt(n)) + 1):
            if n % m == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(n)

    for word in sentence.split(' '):
        for n in primes:
            if len(word) % n == 0:
                result.append(word)
                break
    return ' '.join(result)
