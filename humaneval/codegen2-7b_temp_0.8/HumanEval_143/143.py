
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
    w_list = sentence.split(" ")
    w_len = len(w_list)

    res = ""
    for i in range(w_len):
        for j in range(w_len):
            if i == j:
                continue
            if w_list[i] == w_list[j]:
                break
            res += w_list[j]
            break
    return res

