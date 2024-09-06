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
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words of prime lengths, in the original order.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []  # Container to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a sentence

# Testing the function
print(words_in_sentence("Let's play a game"))  # Expected output: "Let's"
print(words_in_sentence("This is a test"))  # Expected output: "is"
```

This script includes a `is_prime` function for checking whether a number is prime or not. The `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then joins the prime words to form a new sentence. The output correctly extracts words with prime lengths from the input sentences.