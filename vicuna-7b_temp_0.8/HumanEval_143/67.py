
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
    # Take a copy of the sentence
    sentence = sentence.copy()

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters in the sentence
    for i in range(len(sentence)):
        # If the current character is a space, append the previous word to the result
        if sentence[i] == " ":
            result += sentence[i-1]
            continue

        # Otherwise, append the current character to the result
        result += sentence[i]

    return result