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
        sentence (str): Input sentence with spaces.

    Returns:
        str: Sentence with only words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # Join prime words to form new sentence
```

This function leverages a `is_prime` function to determine if a number is prime. It then checks the length of each word in the sentence to see if it's prime, and collects them into a new list. Finally, it joins these prime words back into a new sentence, in the original order. This solves the problem of extracting words from a sentence that have prime lengths while maintaining the original sentence's structure and order.