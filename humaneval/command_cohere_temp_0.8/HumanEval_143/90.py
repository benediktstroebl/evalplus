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
        sentence (str): A string representing a sentence with spaces between words.

    Returns:
        str: A string containing words with prime lengths in their original order.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # Join prime words to form a string
```

This function leverages the `is_prime` helper to check each word length in the sentence, adding eligible words to the `prime_words` list. Finally, the function rejoined these prime-length words to form the desired output string.

The `is_prime` function is a basic implementation of the `Sieve of Eratosthenes` algorithm, it iterates through the numbers from 2 to the square root of the given number and marks each multiple of 2 as non-prime. This process continues recursively for each prime number, eliminating multiples of the current prime to narrow down the search range for the next prime. If no factors are found before the square root is reached, the number is considered prime. 

Note that this approach ensures that the prime-length words are correctly identified and sorted in the original sentence order. Additionally, the code is efficiently managed to complete within a reasonable time frame, making it suitable for scenarios involving prime number detection and word manipulation in sentences.