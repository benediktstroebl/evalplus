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
        sentence (str): A sentence with spaces between words.

    Returns:
        str: A new sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split sentence into a list of words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This function leverages the `is_prime` helper to check whether the length of each word is prime or not, words that meet this condition are then aggregated in the `prime_words` list, and finally, joined together to form a new sentence where words with prime lengths retain their original order. 

The `is_prime` function uses a optimized brute-force approach for checking primality: it iterates from 2 to the square root of the number and checks for divisibility, if a number is divisible by any integer in this range it's not prime, if it's not divisible by any integer in this range it's prime. 

This approach results in a very efficient primality test for large numbers, the complexity of `is_prime` is O(sqrt(n)), and it's enough for checking primality for word lengths which are typically small. 

This code has a time complexity of O(n*sqrt(n)) where n is the total number of characters in the input sentence, as it iterates through each character once and for each character performs a sqrt(n) traversal in the divisibility check. 

Please note that the code works as expected for sentences with a maximum length of 100 characters since the constraint states that the input sentence can contain up to 100 characters. 

If you expect to handle longer text in the future you may consider using more efficient primality testing algorithms, like the Sieve of Eratosthenes, to make sure the code remains efficient.