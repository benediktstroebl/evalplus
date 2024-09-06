
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
    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    words_list = sentence.split(" ")
    for index, word in enumerate(words_list):
        if len(word) == 0:
            del words_list[index]
        elif len(word) == 1:
            words_list[index] = word
        else:
            for prime_num in prime_nums:
                if prime_num == len(word):
                    words_list[index] = word
                    break

    return " ".join(words_list)
