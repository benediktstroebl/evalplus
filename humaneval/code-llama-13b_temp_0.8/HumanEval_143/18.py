
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
    # A list containing prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    # A list containing the words in the original sentence
    words_in_sentence = sentence.split()
    # A list containing the words in the original sentence with a length prime number
    words_in_sentence_length_prime_number = []
    # A list containing the words in the original sentence with a length that is not prime number
    words_in_sentence_length_not_prime_number = []
    # For each word in the list of the words in the original sentence
    for word in words_in_sentence:
        # If the length of the word is a prime number
        if len(word) in primes:
            # Append the word in the list containing the words in the original sentence with a length prime number
            words_in_sentence_length_prime_number.append(word)
        # If the length of the word is not a prime number
        else:
            # Append the word in the list containing the words in the original sentence with a length that is not prime number
            words_in_sentence_length_not_prime_number.append(word)
    # A variable containing the final string
    result = ''
    # For each word in the list containing the words in the original sentence with a length prime number
    for word in words_in_sentence_length
