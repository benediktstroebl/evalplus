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
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words of prime lengths, in the original order.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []  # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a sentence

# Test cases
print(words_in_sentence("This is a test"))  # Output: 'is'
print(words_in_sentence("lets go for swimming"))  # Output: 'go for'
```

This script includes a `is_prime` function to check if a number is prime or not, which is used by the `words_in_sentence` function to extract words from a sentence that have prime lengths. The `words_in_sentence` function splits the sentence into words, checks each word's length for primality, and then joins the prime words back together to form a new sentence. The prime words are stored in the `prime_words` list and joined together using ' '.join(prime_words).

The script also features test cases to validate the function's behavior; the test cases are placed in comments, and you can uncomment them and adapt them to your needs.