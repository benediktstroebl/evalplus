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
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words whose lengths are prime numbers.
    """
    words = sentence.split() 
    result = "" 

    for word in words:
        if is_prime(len(word)):
            result += word + " " 

    return result