
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
    # pylint: disable=R0911, R0912
    # R0911: too-many-return-statements
    # R0912: too-many-branches
    words = sentence.split()
    if len(words) == 1:
        return words[0]

    if len(words) == 2:
        word1, word2 = words
        if is_prime(len(word1)) and is_prime(len(word2)):
            return word1 + " " + word2
        if is_prime(len(word1)):
            return word1
        return word2

    if len(words) == 3:
        word1, word2, word3 = words
        if is_prime(len(word1)) and is_prime(len(word2)) and is_prime(len(word3)):
            return word1 + " " + word2 + " " + word3
        if is_prime(len(word1)) and is_prime(len(word2)):
            return word1 + " " + word2
        if is_prime(len(word1)) and is_prime(len(word3)):
            return word1 + " " + word3
        if is_prime(len(word2)) and is_prime(len(word3)):
            return word2 + " " + word3
        if is_prime(len(word1)):
            return word1
        if is_prime(len(word2)):
            return word2
        return word3

    if len(words) == 4:
        word1, word2, word3, word4 = words
        if is_prime(len(word1)) and is_prime(len(word2)) and is_prime(len(word3)) and is_prime(len(word4)):
            return word1 + " " + word2 + " " + word3 + " " + word4
        if is_prime(len(word1)) and is_prime(len(word2)) and is_prime(len(word3)):
            return word1 + " " + word2 + " " + word3
        if is_prime(
