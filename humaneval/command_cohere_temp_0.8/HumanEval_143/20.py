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
        sentence (str): Input sentence with spaces as delimiters.

    Returns:
        str: A sentence with words of prime lengths, keeping the original order.

    Example:
        Input: "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a sentence
```

This `is_prime` function is used to determine if a number is prime. It does so by iterating from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of these integers, it's not a prime; otherwise, it is a prime. This foundational primality test is used as a building block for more complex primality tests, ensuring numbers are correctly identified as prime or not. 

The `words_in_sentence` function leverages this primality test to parse through each word in a given sentence. When given a sentence as input, the function first splits it into individual words using spaces as delimiters. It then screens each word's length to confirm if it's prime. Prime words are collected in the `prime_words` list. Finally, the function rejoins these prime words into a new sentence, preserving the original order as dictated by the input. 

Such a solution adheres to the problem's prompt, providing a function that leverages primality testing to extract words from a sentence that have prime lengths, all while maintaining the original sentence's structure and word order.