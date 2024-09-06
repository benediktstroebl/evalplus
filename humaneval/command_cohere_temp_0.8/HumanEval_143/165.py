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
    Extracts words from a sentence with prime lengths.

    Args:
        sentence (str): Input sentence with spaces as delimiter.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []  # Container for prime-length words

    for word in words:
        if is_prime(len(word)):  # Check word length for primality
            prime_words.append(word)

    return ' '.join(prime_words)  # Rejoin prime words into a sentence
```

This function leverages the `is_prime` helper to check if the length of each word in the sentence is prime. It then compiles a list of those prime-length words and rejoins them into a sentence, preserving the original word order.

Ensure that the `is_prime` function is correctly defined and that you have the math module installed, as import `math` is required for the code to run properly.