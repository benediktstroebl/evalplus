
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
    sentence_list = sentence.split(" ")
    prime_list = []
    for word in sentence_list:
        if len(word) <= 2:
            continue
        if all(i <= 2 for i in word):
            prime_list.append(word)
    return " ".join(prime_list)

