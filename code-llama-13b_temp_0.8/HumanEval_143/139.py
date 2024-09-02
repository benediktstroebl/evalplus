
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
    primes = [True] * (101)
    for i in range(2, 101):
        for j in range(2 * i, 101, i):
            primes[j] = False

    primes[0] = False
    primes[1] = False
    primes[2] = True
    result = ''
    for word in words:
        if primes[len(word)]:
            result += ' ' + word if result else word
    return result.strip()

