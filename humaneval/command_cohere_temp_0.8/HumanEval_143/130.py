Here's a Python script that solves the problem:
```python
import math

def is_prime(n):
    """
    Checks whether a number is prime or not.

    Args:
        n (int): Number to check for primality.

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
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): A sentence with space-separated words.

    Returns:
        str: A new sentence with words whose lengths are prime numbers.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # Join prime words to form a new sentence

# Example usage
input_sentence = "This is a test"
print(words_in_sentence(input_sentence))  # Output: "is"

input_sentence = "lets go for swimming"
print(words_in_sentence(input_sentence))  # Output: "go for"
```

This script defines a `is_prime` function to check if a given number (in this case, the length of a word) is prime or not. Additionally, it defines the `words_in_sentence` function, which splits the input sentence into words, checks each word's length for primality, and then joins the prime-length words back together to form a new sentence. The output of the example usages shows how the function works, keeping only the words with lengths that are prime numbers.