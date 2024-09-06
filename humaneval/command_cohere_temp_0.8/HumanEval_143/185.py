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
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []           # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check word length for primality
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

The `is_prime` function is used to determine whether a given number is prime or not. It iterates from 2 up to the square root of the number, checking for divisibility. If the number is divisible by any integer within this range, it's not prime; otherwise, it is prime. This fundamental primality-checking function is used to examine the lengths of words in the `words_in_sentence` function.

The `words_in_sentence` function takes an input sentence and splits it into words using spaces as the delimiter. It initializes an empty list called `prime_words` to store words whose lengths are prime numbers. The function then iterates through each word in the sentence, checking its length using the `is_prime` function. If the length is prime, the word is added to the `prime_words` list. Finally, the function joins the prime words back into a sentence using a space as the delimiter and returns the resulting string.

The provided code efficiently solves the problem by identifying words in the sentence that have prime lengths and reorganizing them into a new sentence while maintaining their original order.