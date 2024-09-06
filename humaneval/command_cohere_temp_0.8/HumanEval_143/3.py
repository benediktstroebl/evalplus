Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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
        sentence (str): The input sentence with words separated by spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = [word for word in words if is_prime(len(word))]  # Check each word length for primality

    return ' '.join(prime_words)  # Join prime words with space to form the new sentence
```

This script defines a function `words_in_sentence` that solves the problem as described. It operates on a provided sentence and returns a new sentence with words whose lengths are prime numbers. It also includes an `is_prime` function for primality checking.

Note that this approach uses a common Python optimization: since the length of a string is always an integer, we can compute the square root of the length using the `int(n**0.5)` expression. Then, in the loop, we only check divisors up to the square root, rather than checking all numbers from 2 to the length.