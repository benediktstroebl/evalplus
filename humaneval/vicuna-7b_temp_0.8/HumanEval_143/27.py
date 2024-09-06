
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
    # split the string into a list of words
    words = sentence.split()
    # initialize an empty list to store the result
    result = []
    # iterate over the words and check if they are prime
    for word in words:
        # check if the length of the word is prime
        if len(str(int(word))) % 1 == 0:
            result.append(word)
    return " ".join(result)