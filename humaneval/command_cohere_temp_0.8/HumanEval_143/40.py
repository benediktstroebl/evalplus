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
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Testing the function
print(words_in_sentence("Let's meet at the zoo for a picnic."))
```

In this code:
- The `is_prime` function checks whether a number (in this case, the length of a word) is prime or not in O(sqrt(n)) time complexity.
- The `words_in_sentence` function splits the input sentence into words and then checks each word's length for primality.
- The output will contain the words from the original sentence that have prime lengths, preserving the original sentence's word order.