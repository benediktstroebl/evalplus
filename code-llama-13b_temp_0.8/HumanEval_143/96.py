
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
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199}

    def is_prime(n):
        if n in primes:
            return True

        if n < 2:
            return False

        if n % 2 == 0:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False

        primes.add(n)
        return True

    sentence = sentence.split()
    result = []
    for w in sentence:
        if len(w) in primes:
            result.append(w)

    return ' '.join(result)

