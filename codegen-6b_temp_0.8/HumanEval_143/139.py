
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
    # naive
    # from collections import Counter
    # count = Counter()
    # for word in sentence.split():
    #     count[word] += 1
    # for word in count:
    #     if (
    #         all(ord(c) < 128 for c in word)
    #         and count[word] == 1
    #     ):
    #         yield word
    #
    # return
    #
    # better
    words = sentence.split()
    return ' '.join(filter(lambda w: is_prime(len(w)), words))

