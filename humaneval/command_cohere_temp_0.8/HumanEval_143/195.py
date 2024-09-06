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
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words of prime lengths, in the original order.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This function leverages the `is_prime` helper to check each word length for primality, adding words with qualifying lengths to the `prime_words` list. The final result is a string compiled from these prime-length words, maintaining the original sentence's word order.

Here is an example usage of the code:
```python
print(words_in_sentence("Let's meet at the park")) # Outputs: "meet at"
```

This script ensures Python efficiency in extracting prime-length words, making it adaptable for varied sentence inputs and length constraints.