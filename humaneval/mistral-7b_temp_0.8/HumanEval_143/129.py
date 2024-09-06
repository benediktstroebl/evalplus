
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

    # Remove punctuation and convert string to lowercase
    sentence = sentence.replace(".", "").replace(",", "").lower()

    # Split sentence into list of words
    words = sentence.split()

    # Initialize list to store prime words
    prime_words = []

    # Iterate over list of words and check if length is prime
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    # Join prime words into a string and return the result
    return " ".join(prime_words)

