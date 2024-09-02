
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
    # Convert string into list of words
    sentence = sentence.split()
    # Create list to store prime numbers
    prime_list = []
    # Create list to store prime words
    prime_words = []
    # Loop through sentence and check if word is prime
    for word in sentence:
        if is_prime(len(word)):
            prime_list.append(word)
    # Loop through prime list and store words into new list
    for word in prime_list:
        if word in sentence:
            prime_words.append(word)
    # Join words and return sentence
    return " ".join(prime_words)

