
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
    #################
    # MEMORY & COUNT #
    #################

    # count_primes = [0] * 100 # O(N)
    # for i in range(2, 100):
    #     if count_primes[i]:
    #         continue
    #     count_primes[i] = i
    #     for j in range(i * 2, 100, i):
    #         count_primes[j] = 0

    # count_prime_word_length = [0] * 100 # O(N)
    # for word in sentence.split():
    #     if len(word) == 1:
    #         continue
    #     if count_primes[len(word)]:
    #         count_prime_word_length[len(word)] += 1

    ###########
    # PATTERN #
    ###########
    words = sentence.split()
    primes = [x for x in range(2, 100) if all([x % i != 0 for i in range(2, x)])]
    return ' '.join([w for w in words if len(w) in primes])

