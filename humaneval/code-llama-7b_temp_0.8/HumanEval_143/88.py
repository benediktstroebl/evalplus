
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
    # Return a list with words whose lengths are prime numbers.
    # The order of the words should be the same as the original sentence
    # words = sentence.split(" ")
    # return [word for word in words if is_prime(len(word))]
    
    # Return a string with words whose lengths are prime numbers.
    # The order of the words should be the same as the original sentence
    return " ".join([word for word in sentence.split(" ") if is_prime(len(word))])
