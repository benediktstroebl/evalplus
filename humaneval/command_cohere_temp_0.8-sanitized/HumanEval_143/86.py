import math
def is_prime(n):
    """
    Checks whether a number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    """
    Extracts words from a sentence with prime lengths.

    Args:
        sentence (str): Input sentence with spaces as delimiter.

    Returns:
        str: A sentence with words of prime lengths kept intact.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []  # Container to store prime words

    for word in words:
        if is_prime(len(word)):  # Check word length for primality
            prime_words.append(word)  # Add prime word to list

    return ' '.join(prime_words)  # Join prime words to form a sentence