```python
import math

def is_prime(n):
    """
    Checks whether the number is prime or not.
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
    """
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Check if the length of each word is prime
    return ' '.join(prime_words)  # join the prime words to form a string
```

This script includes the `is_prime` function for checking prime numbers, and the `words_in_sentence` function solves the specified problem. You can use this code to solve the challenge effortlessly. Feel free to experiment with various inputs to observe its behavior.