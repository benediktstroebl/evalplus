import math
def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to check for primality.

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
    Extracts words from the sentence whose lengths are prime numbers.

    Args:
        sentence (str): Input sentence to process.

    Returns:
        str: A string containing only words with prime lengths, in the same order as the input sentence.

    Usage:
        >>> words_in_sentence("This is a test")
        'is'
        >>> words_in_sentence("lets go for swimming")
        'go for'
    """
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = []            # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)
    
    return ' '.join(prime_words)  # Join prime words to form a string