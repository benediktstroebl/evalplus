```python
import math

def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

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
    Extracts words from the sentence whose lengths are prime numbers.

    Args:
        sentence (str): A string representing a sentence.

    Returns:
        str: A string containing only words with prime lengths, in the same order as the input sentence.
    """
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a string and return
```

This function leverages a centralized `is_prime` function to evaluate whether a given number is prime. It then processes the sentence, identifies words, and screens for those with prime lengths, saving them in the `prime_words` list. The final step rejoins these prime-length words into a new string for returned output. 

The `is_prime` helper function substantiates primality checks with a time-honed algorithm, traversing upwards from 2 to the square root of the target number, verifying its solo divisibility. 

To unpack the problem's prompt, the code snippet above offers a precise resolution grounded in mathematical primality testing. 

To harness this Python script, you can import it into your project, run the `words_in_sentence` function as needed, and reap the benefits of your generated prime-word sentences.