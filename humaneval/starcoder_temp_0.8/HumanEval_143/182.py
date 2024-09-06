
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

    def is_prime(x):
        """
        Time Complexity: O(sqrt(x))
        """
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    def get_words(sentence):
        return sentence.split()

    def get_primes(words):
        return list(filter(is_prime, map(len, words)))

    def get_primes_words(words, primes):
        return list(filter(lambda x: len(x) in primes, words))

    def get_primes_sorted(words, primes):
        return sorted(
            get_primes_words(words, primes),
            key=lambda x: words.index(x)
        )

    words = get_words(sentence)
    primes = get_primes(words)
    return''.join(get_primes_sorted(words, primes))

