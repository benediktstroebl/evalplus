Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
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
        sentence (str): A string representing a sentence with spaces between words

    Returns:
        str: A new sentence with words whose lengths are prime numbers

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split()  # split the sentence into a list of words
    prime_words = []  # a list to store prime words

    for word in words:
        if is_prime(len(word)):  # check if the length of the current word is prime
            prime_words.append(word)  # if yes, add it to the list

    return ' '.join(prime_words)  # join the prime words list to form a string and return
```

This script defines a function `words_in_sentence` that takes a sentence as input and returns a new sentence with words whose lengths are prime numbers.

The script also defines a helper function `is_prime` that checks if a given number (in this case, the length of a word) is prime or not. This function will be used inside `words_in_sentence`.

Both functions are self-contained and do not rely on any external variables, making them ready for immediate use. 

This solution will pass the test cases corresponding to the provided problem statement. 
Let's break down the solution and highlight the steps and logic with annotations on each line: 
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False  # If n is less than or equal to 1, it's not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # If n is divisible by any number from 2 to its square root, it's not prime
    return True  # If n is not divisible by any number from 2 to its square root, it's prime
```

The `is_prime` function takes an integer `n` as input and returns `True` if `n` is prime, and `False` otherwise. The function first checks if `n` is less than or equal to 1, returning `False` in this case since prime numbers must be greater than 1. It then iterates from 2 up to the square root of `n` (inclusive), checking whether `n` is divisible by any number within this range. If `n` is divisible by any of these numbers,