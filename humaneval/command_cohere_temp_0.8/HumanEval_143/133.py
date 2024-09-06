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
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Testing the function
sentence = "This is a test"
print(words_in_sentence(sentence))  # Expected: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Expected: "go for"
```

This script includes the `is_prime` function for checking primality, which is used by `words_in_sentence` to extract words with prime lengths from the input sentence.

When you run the script, it will print the desired output as specified in the given examples.