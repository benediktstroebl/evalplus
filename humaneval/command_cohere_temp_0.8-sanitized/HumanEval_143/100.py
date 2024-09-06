import math
def is_prime(n):
    """
    Checks whether the given integer is a prime number or not.

    Args:
        n (int): Integer to check for primality.

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
    words = sentence.split()  # Split the sentence into words using spaces as separators
    prime_words = []          # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words
    
    return ' '.join(prime_words)  # Join prime words to form a single string and return