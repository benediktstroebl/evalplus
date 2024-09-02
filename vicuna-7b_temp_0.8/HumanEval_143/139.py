
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
    sentence = sentence.lower()
    words = sentence.split()
    words_list = []
    for word in words:
        if len(word) > 1:
            words_list.append(word)
    for i in range(1, len(words_list)):
        for j in range(i+1, len(words_list)):
            if (words_list[i] < words_list[j]) and (words_list[j] % words_list[i] == 0):
                words_list[i], words_list[j] = words_list[j], words_list[i]
    new_sentence = " ".join(words_list)
    return new_sentence
