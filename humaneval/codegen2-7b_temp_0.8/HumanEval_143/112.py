
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
    sentence_list = sentence.split()
    prime_number = [True for _ in range(len(sentence_list))]
    for i in range(len(sentence_list)):
        if prime_number[i]:
            sentence_list[i] = sentence_list[i][::-1]
        sentence_list[i] = sentence_list[i][1:]
    return " ".join(sentence_list)

