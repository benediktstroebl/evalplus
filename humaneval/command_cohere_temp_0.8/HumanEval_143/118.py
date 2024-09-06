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
        sentence (str): Input sentence with spaces as delimiters.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []  # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a sentence
```

This script includes the `is_prime` function for checking prime numbers, and the `words_in_sentence` function appropriately processes the input sentence to return a new sentence with words of prime lengths.

Ensure you have the `math` module imported to use the `math.sqrt()` function for the primality check. You can run the code with test cases to verify it works as expected. Adjust the test cases to cover various scenarios and edge cases to thoroughly test the solution.