
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
    # if len(sentence) < 2:
    #     return sentence
    #
    # prime_numbers = [2, 3, 5, 7]
    # sentence = sentence.split(" ")
    #
    # # for word in sentence:
    # #     if len(word) in prime_numbers:
    # #         new_sentence.append(word)
    # # return " ".join(new_sentence)
    #
    # prime_numbers = [2, 3, 5, 7]
    # words = [word for word in sentence if len(word) in prime_numbers]
    # return " ".join(words)


    words = filter(lambda word: len(word) in [2, 3, 5, 7], sentence.split())
    return " ".join(words)

