```python
import math

def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check if prime

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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A string containing words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)
```

This function `is_prime` checks whether a given number is prime or not, and the function `words_in_sentence` takes a sentence as input, splits it into words separated by spaces, and then checks the length of each word, keeping the ones that are prime numbers, and re-joining them with a space as the original sentence.

Note that the `is_prime` function may not cover all edge cases, as there are various sophisticated techniques for checking primality in number theory. This function should be sufficient for this specific problem and its constraints.  Also, this function assumes that the sentence contains only letters and spaces, if the sentence contains other characters, you might need to add additional checks.