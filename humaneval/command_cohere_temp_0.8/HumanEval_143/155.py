Here is a Python script with a self-contained function that solves the problem:
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
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```
This script defines a function `words_in_sentence()` that splits the input sentence into words, checks each word's length for primality, and then recombines the prime-length words to form a new sentence in the same order. 
The primality check is implemented by the `is_prime()` function which iterates through divisors up to the square root and returns `True` if the number is prime. 

The `words_in_sentence()` function should correctly solve the problem statement given in the markdown code block. It handles various sentence lengths and compositions of prime and non-prime word lengths.