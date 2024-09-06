```python
import math

def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): Input sentence.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This script includes the `is_prime` function which is used to identify prime numbers. The `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then recombines the prime-length words into a new string. The resulting solution effectively extracts prime-length words from the input sentence. 

The provided code seems to accurately address the specified problem and should yield the desired output.