Here is a Python script with a self-contained function that solves the problem:
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
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Test the prime checker and main function
def test_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True

test_primes()

# Test the main function with examples from the prompt
assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
```

This script defines a `is_prime` function to check if a number is prime or not. It then defines the `words_in_sentence` function to split the sentence into words, and then filters out the words whose length is a prime number. The function then joins these filtered words to produce the output string. The `test_primes` function is an auxiliary function to test the `is_prime` function. You can uncomment it and run it to see if the `is_prime` function behaves as expected. Finally, the last assertion tests the `words_in_sentence` function with the examples provided in the prompt.