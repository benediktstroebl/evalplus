```python
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
        sentence (str): A string representing a sentence with spaces between words.

    Returns:
        str: A string containing words with prime lengths in their original order.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This script includes the `is_prime` function for primality checking and solves the given problem using a space-separated string (`sentence`) as input, which is then split into a list of words (`words`). It iterates through each word, checking its length for primality using the `is_prime` function, and eventually returns a string (`prime_words`) comprising only prime-length words concatenated with spaces. The output maintains the original order of words from the input sentence.