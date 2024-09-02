
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
    arr = sentence.split(' ')
    result = []

    for elem in arr:
        if len(elem) > 1:
            primes = [2, 3, 5, 7, 11, 13, 17, 19]
            for prime in primes:
                if len(elem) % prime == 0:
                    result.append(elem[:prime])
                    break

    return ' '.join(result)
