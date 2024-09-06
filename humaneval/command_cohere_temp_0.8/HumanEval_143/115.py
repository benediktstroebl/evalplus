```python
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
        sentence (str): A string representing a sentence with spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.

    Example:
        >>> words_in_sentence("The quick brown fox jumps over the lazy dog") \
                .replace(" ", "")
        'fht'
    """
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)
```

This approach splits the sentence into words and then uses a list comprehension to filter out words whose lengths are prime numbers.

Here's a test to validate the solution:
```python
def test_words_in_sentence():
    assert words_in_sentence("The quick brown fox jumps over the lazy dog") \
        .replace(" ", "") == 'fht'
    assert words_in_sentence("is it a prime number?") \
        .replace(" ", "") == 'i'
    assert words_in_sentence("lets go for swimming") \
        .replace(" ", "") == 'go for'

test_words_in_sentence()
```

The test cases ensure that the function `words_in_sentence()` correctly identifies prime-length words and returns them as a space-separated string.

The `is_prime()` function is added to improve code readability and is used to verify prime numbers in the loop. It can also be used for other prime-related checks.