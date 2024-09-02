
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
    result = []
    split = sentence.split()

    # Get all unique characters in the sentence
    unique_list = []
    for word in split:
        unique_list.extend(set(word))

    # Check if characters in unique_list are prime
    for character in unique_list:
        if not is_prime(int(character)):
            return ''.join(char for char in split if char != character)

    return ''.join(char for char in split if char in unique_list)


assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
