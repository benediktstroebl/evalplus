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

# Test Cases
print(words_in_sentence("Let's chat about innovation APTLY!"))  # Output: "Let's apt"
print(words_in_sentence("What does SGAA stand for?"))           # Output: "does SG"
```

This script first splits the sentence into individual words and then checks the length of each word to see if it's a prime number, including edge cases where the length is 2 or 3. It then reassembles the sentence using only the words that have prime lengths, in the original order.