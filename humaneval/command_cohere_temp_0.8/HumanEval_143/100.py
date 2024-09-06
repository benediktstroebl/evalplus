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
        sentence (str): Input sentence with spaces.

    Returns:
        str: Sentence with only words of prime lengths.
    """
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Test the solution with provided examples
assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
```

This script includes a `is_prime` function for primality testing and the `words_in_sentence` function to solve the problem. The test cases ensure the function behaves as expected. You can use this code to implement the solution and run it with various inputs. If you need guidance integrating it with a test suite or other improvements, feel free to ask.