Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the integer 'n' is a prime number or not.

    Args:
        n (int): Number to be checked.

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
        sentence (str): The input sentence.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    words = sentence.split()  # Split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Check the lengths of each word
    return ' '.join(prime_words)  # Join prime words back into a string
```

This script includes a `is_prime` function that checks if a number is prime or not. The `words_in_sentence` function then splits the sentence into words, checks the primality of each word's length using the previous function, and then joins the prime words back into a string.

The `example_tests.py` file contains example tests that can be used to validate the correctness of the `words_in_sentence` function:
```python
def test_example_1():
    sentence = "This is a test"
    expected = "is"
    result = words_in_sentence(sentence)
    assert result == expected

def test_example_2():
    sentence = "lets go for swimming"
    expected = "go for"
    result = words_in_sentence(sentence)
    assert result == expected
```