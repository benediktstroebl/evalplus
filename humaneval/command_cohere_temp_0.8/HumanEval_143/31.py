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
        str: A string containing words with prime lengths in their original order.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split the sentence into words using spaces as separators
    prime_words = []           # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a string and return
```

This script includes a `is_prime` function to check if a given number is prime or not. Additionally, the `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then joins the prime words back together to form a string. 

The output will contain primally sized words from the input sentence, in the original order. For instance, given the input sentence "This is a test," the function will return the output: "is."