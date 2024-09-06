```python
import math

def is_prime(n):
    """
    Checks whether the given integer is a prime number or not.

    Args:
        n (int): Integer to check for primality.

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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This script includes the `is_prime` function for primality testing, and the `words_in_sentence` function applies this testing to separate words in the sentence and then recombines them into a new string containing only prime-length words. The `is_prime` function is used to check if a given number is a prime number or not. It does this by first checking if the number is less than or equal to 1, in which case it returns `False` as prime numbers always exceed 1. Then, it iterates from 2 up to the square root of the number, checking if the number is divisible by any of these integers. If it is, then it returns `False`, indicating that the number is not prime. If the loop completes without finding a divisor, then it returns `True`, indicating that the number is prime. 

The `words_in_sentence` function uses this `is_prime` function to filter out words in the sentence that have prime lengths. It splits the sentence into a list of words, then iterates through each word in the list, checking if its length is prime using the `is_prime` function. If a word has a prime length, it's added to the `prime_words` list. Finally, the function joins the prime words back into a string and returns it. 

Overall, this solution provides a clear and efficient way to solve the problem statement. 

Note: The `is_prime` function used here is indeed efficient for primality testing, with a time complexity of O(sqrt(n)) as indicated, but is not the most efficient method possible. Some alternatives like the 'Sieve of Eratosthenes' algorithm would provide an even faster primality test, but the given solution still maintains an acceptable time complexity and is well-suited for this specific problem.