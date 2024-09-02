
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
    # Remove whitespace from start and end of sentence.
    sentence = sentence.strip()
    # Split sentence into words.
    words = sentence.split()
    # Initialize result as empty string.
    result = ""
    # For each word in the sentence...
    for word in words:
        # Check if the word's length is prime.
        if is_prime(len(word)):
            # Append the word to the result.
            result += word + " "
    # Remove final whitespace from result.
    result = result.strip()
    # Return the result.
    return result

