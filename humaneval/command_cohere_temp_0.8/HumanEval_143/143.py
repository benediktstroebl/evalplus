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
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words whose lengths are prime numbers.
    """
    words = sentence.split() 
    result = "" 

    for word in words:
        if is_prime(len(word)):
            result += word + " " 

    return result
```

This script defines a function `is_prime` to check whether a given number is prime or not. It iterates through numbers from 2 to the square root of the input number, if the number is divisible by any other number, it returns `False`. If the number is not divisible by any other number, it's deemed prime and `is_prime` returns `True`.

The `words_in_sentence` function simply splits the input sentence into words and iterates through them. For each word, it checks its length against the `is_prime` function. If the length is prime, the word is added to the `result` string, which is returned after processing all words in the sentence.