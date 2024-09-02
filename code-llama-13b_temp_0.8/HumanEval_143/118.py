
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
    words = sentence.split()
    words_with_prime_length = []
    for word in words:
        if len(word) == 1 or len(word) == 2:
            continue
        flag = True
        for i in range(2, len(word)):
            if (word[i] == word[0]) and (word[i] == word[1]):
                flag = False
                break
        if flag and (len(word) > 1):
            words_with_prime_length.append(word)
    return " ".join(words_with_prime_length)

