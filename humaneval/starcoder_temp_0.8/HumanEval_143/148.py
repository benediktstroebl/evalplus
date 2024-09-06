
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
    # convert to list of words
    words = sentence.split(" ")
    # remove all non-letters from words
    words = list(map(lambda x: re.sub('[^a-zA-Z0-9 ]', '', x), words))
    # remove all empty strings from list
    words = list(filter(None, words))
    # convert to list of numbers
    words = list(map(int, words))
    # remove all numbers that are not prime
    words = list(filter(is_prime, words))
    return " ".join(list(map(str, words)))

