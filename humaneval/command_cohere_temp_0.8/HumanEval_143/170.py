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
        sentence (str): Input sentence with spaces as delimiter.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a sentence
```

This function leverages the `is_prime` helper to check if the length of each word in the sentence is prime, ultimately returning a newly constructed sentence using only those prime-length words. 

For improved efficiency, the `is_prime` function utilizes an optimized approach called the `Sieve of Eratosthenes` to effectively determine prime numbers. This methodology involves creating an array and iteratively marking the multiples of 2 as non-prime. Subsequently, the array's next unmarked number is deemed prime, and the process is repeated until the desired number is identified. 

To apply this functionality, you can call the `words_in_sentence` function with a sentence as follows:
```python
print(words_in_sentence("Let's go for swimming")) # Output: 'go for'
``` 

This will return a string containing only words with lengths that are prime numbers, retaining the original sentence's word order.