
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
    words_with_length_that_are_prime = []
    for word in words:
        if len(word) > 1:
            for i in range(2, int(len(word) ** 0.5) + 1):
                if len(word) % i == 0:
                    break
            else:
                words_with_length_that_are_prime.append(word)
    return " ".join([word for word in words_with_length_that_are_prime if word in words])