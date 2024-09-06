
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
    # raise NotImplementedError()
    words = sentence.split()
    # new_words = []
    # for word in words:
    #     if all(i > 1 for i in [len(word) for word in str(word)]):
    #         new_words.append(word)
    new_words = [word for word in words if all(i > 1 for i in [len(word) for word in str(word)])]
    return " ".join(new_words)


