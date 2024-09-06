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
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This Python script defines a function `words_in_sentence` that accepts a string representing a sentence and returns a new sentence consisting of words whose lengths are prime numbers.

The script also includes a separate function `is_prime` to check whether a number is prime or not. This function is used by `words_in_sentence` to determine whether a word's length is prime. 

Both functions are equipped with docstrings to describe their purposes and functionalities. 

This solution adheres to the problem's constraints and delivers the required functionality while maintaining clarity and readability.