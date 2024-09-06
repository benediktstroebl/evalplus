import math
def is_prime(n):
    """
    Checks whether the given number is a prime or not.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    # Split the sentence into words using space as the delimiter
    words = sentence.split()
    # Initialize an empty list to store the prime words
    prime_words = []
    # Iterate over each word in the sentence
    for word in words:
        # Get the length of the current word
        word_length = len(word)
        # Check if the length of the current word is prime
        if is_prime(word_length):
            # If the word length is prime, add the word to the list of prime words
            prime_words.append(word)
    # Join the prime words to form a single string
    result = ' '.join(prime_words)
    # Return the resulting string
    return result