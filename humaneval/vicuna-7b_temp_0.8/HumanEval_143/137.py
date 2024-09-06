
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
    # initialize new string with empty spaces
    new_string = ""

    # iterate through each character of the sentence
    for char in sentence:
        # check if the current character is a letter
        if char.isalpha():
            # if it's a letter, append it to the new string
            new_string += char

            # check if the length of the new string is prime
            if len(new_string) % 2 != 0:
                # if it's not prime, append a space and keep iterating
                new_string += " "
            else:
                # if it's prime, break out of the loop
                break

    # return the new string
    return new_string
