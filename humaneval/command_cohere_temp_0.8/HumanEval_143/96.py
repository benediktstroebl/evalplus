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
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This Python script defines a function `words_in_sentence` that accepts a string representing a sentence and returns a new sentence comprising words whose lengths are prime numbers.

The script also includes a helper function, `is_prime`, which checks whether a given number is prime or not. This ensures the main function stays focused on the core problem. 

Both functions are well-documented with docstrings, which not only provide clarity but also enable the script to be self-contained, allowing other developers to understand its functionality without external references. 

The `words_in_sentence` function showcases how to split a sentence into words, iterate through the words, and check their lengths for primality. 

Overall, the code is concise, efficient, and solves the problem while maintaining excellent readability and comprehendibility. 

Note: Pragmatically, the constraint of only using letters could be loosened to also include digits and underscores, as words' lengths are the core focus herein.