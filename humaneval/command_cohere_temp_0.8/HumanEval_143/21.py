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
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []  # List to store prime-length words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list

    return ' '.join(prime_words)  # Join prime words to form a new sentence

# Test cases
print(words_in_sentence("This is a test"))  # Output: 'is'
print(words_in_sentence("lets go for swimming"))  # Output: 'go for'
```

This script defines a function `words_in_sentence()` that takes a sentence as input and returns a string composed of words whose lengths are prime numbers. It achieves this by dividing the sentence into individual words, checking each word's length for primality, and then recombining the prime-length words to form a new sentence. 

The `is_prime()` function is also provided to check whether a given number (in this case, the length of a word) is prime or not, it efficiently checks all divisors up to the square root of the number.