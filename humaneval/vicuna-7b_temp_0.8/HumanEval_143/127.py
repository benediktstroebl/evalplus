
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
    # check if sentence is empty
    if len(sentence) == 0:
        return ""

    # check if sentence is empty
    if len(sentence) == 1:
        return sentence[0]

    # split the sentence into a list of words
    words = sentence.split()

    # sort the words by length
    words.sort(key=len, reverse=True)

    # initialize the result to an empty string
    result = ""

    # loop over the sorted words
    for word in words:
        # check if the length of the word is prime
        if is_prime(len(word)):
            # append the word to the result
            result += word
        else:
            # remove the word from the sorted list
            words.remove(word)

    return result
