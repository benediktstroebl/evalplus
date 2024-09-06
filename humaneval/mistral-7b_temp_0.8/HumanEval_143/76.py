
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
    import math
    from collections import defaultdict
    words = sentence.split()
    words_len = defaultdict(list)
    for word in words:
        words_len[len(word)].append(word)

    result = ""
    for word_length, words in words_len.items():
        if all(isinstance(word_length, int) for word_length in words):
            if is_prime(word_length):
                result += " " + " ".join(words)
    return result.strip()

