
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
    words = sentence.split(' ')

    def generates_primes(n):
        primes = [True] * (n + 1)
        for i in xrange(2, n):
            if primes[i]:
                j = 2
                while i * j <= n:
                    primes[i * j] = False
                    j += 1
        return [i for i in xrange(2, n) if primes[i]]

    primes = generates_primes(len(words))
    result = ''
    for word in words:
        if len(result) == 0 or result[-1] != word[0]:
            # starts from the first character
            result += word
            continue

        # find the prime number
        for prime in primes:
            if prime <= len(word):
                break

        result += word[prime-1]
    return result

