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
    for i in range(2, int(n ** 0.5) + 1):
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

    Example:
        >>> words_in_sentence("This is a test")
        'is'
    """
    words = sentence.split()  # Split the sentence into words using spaces as separators
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a sentence

# Test the function
def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("Simple and easy as 1 2 3") == "as"
    assert words_in_sentence("Extraordinary!!!!") == "Extraordinary"

test_words_in_sentence()
```

This script includes the primality-checking function `is_prime` and the `words_in_sentence` function described in the problem statement. The `test_words_in_sentence` function provides example tests for the `words_in_sentence` function to ensure its correctness. Adjust the test cases as needed.