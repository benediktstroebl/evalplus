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
    Extracts words from a sentence whose lengths are prime.

    Args:
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A string containing words whose lengths are prime, retaining the original order.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)