
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

    primes = [1]
    for i in range(2, 1001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return''.join([words[i] for i in range(len(words)) if primes[len(words[i])] == 1])
