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
    words = sentence.split()
    result = ""

    for word in words:
        if is_prime(len(word)):
            result += word + " "

    return result
```

This approach leverages the `is_prime` function to check whether a number (in this case, the length of a word) is a prime number. The function iterates through each word in the sentence, and if its length is prime, it adds the word (with a space at the end to separate words in the result) to the `result` string. The final output will contain only the words with prime lengths, presented in the original order. 

The `is_prime` function is a basic implementation of the `Sieve of Eratosthenes` algorithm, it iterates from 2 up to the square root of the number and marks the multiples of 2 as non-prime. For larger numbers, it's efficient to skip multiples of small primes like 2 and 3, and this approach ensures that by marking the multiples of 2 first.