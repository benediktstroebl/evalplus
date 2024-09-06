
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
    # Time: O(n^2)
    # Space: O(n)

    from itertools import combinations_with_replacement, permutations
    from functools import reduce
    from operator import mul

    def is_prime(num):
        if num <= 1:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    items = sentence.split(' ')
    words = []
    for i in range(1, len(items) + 1):
        for j in combinations_with_replacement(items, i):
            words.append(''.join(j))

    words = sorted(list(set(words)))
    result = reduce(mul, [len(w) for w in words if is_prime(len(w))])

    return result
