
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
    # # Initial solutions
    # # # 1
    # def words_in_sentence(sentence):
    #     return " ".join(
    #         [word for word in sentence.split(" ") if len(word) == 2]
    #     )
    # # # 2
    # def words_in_sentence(sentence):
    #     return " ".join(
    #         [word for word in sentence.split(" ") if len(word) in [2, 3, 5, 7, 11, 13]]
    #     )
    # # # 3
    # def words_in_sentence(sentence):
    #     return " ".join(
    #         [word for word in sentence.split(" ") if len(word) not in [4, 6, 8, 9, 10, 12, 14, 15]]
    #     )

    # # Faster solutions
    # # # 4
    # def words_in_sentence(sentence):
    #     return " ".join([word for word in sentence.split(" ") if is_prime_number(len(word))])

    # # # 5
    # def words_in_sentence(sentence):
    #     return " ".join([word for word in sentence.split(" ") if not is_composite_number(len(word))])

    # # # 6
    # def words_in_sentence(sentence):
    #     return " ".join(
    #         [word for word in sentence.split(" ") if is_prime_number(len(word)) and not is_composite_number(len(word))]
    #     )

    # # # 7
    # def words_in_sentence(sentence):
    #     return " ".join(
    #         [word for word in sentence.split(" ") if (is_prime_number(len(word)) and not is_composite_number(len(word))) or (not is_prime_number(len(word)) and is_composite_number(len(word)))]
    #     )

