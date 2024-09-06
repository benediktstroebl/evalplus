
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
    length_list = [len(word) for word in words]
    prime_list = [2, 3]
    result = ""
    for i in range(len(length_list)):
        if length_list[i] % 2 != 0:
            length_list[i] += 1
        for j in range(i+1, len(length_list)):
            if length_list[j] % 2 == 0:
                break
        else:
            length_list[i], length_list[j] = length_list[j], length_list[i]
    for i in length_list:
        result += words[i]
    return result

