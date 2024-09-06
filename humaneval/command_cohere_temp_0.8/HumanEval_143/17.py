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

This Python script includes a `is_prime` function for testing primality and the `words_in_sentence` function that extracts words from a given sentence, testing each word's length for primality. 

The primality test is conducted using a optimized approach, checking divisibility across numbers from 2 to the square root of the length. 

The `words_in_sentence` function splits a space-separated sentence into words, subsequently checking each word's length for primality. Words passing the test are aggregated to produce the returned sentence. 

The code outlined provides an efficient primality test, alongside a function for extracting words with prime lengths from a sentence, demonstrating an adept use of Python for solving the problem.