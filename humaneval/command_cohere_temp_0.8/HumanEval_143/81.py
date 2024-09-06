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
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): A string representing a sentence with spaces separating words.

    Returns:
        str: A string containing words with prime lengths in their original order.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []  # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the current word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a string and return
```

This function leverages the `is_prime` helper to check each word length in the sentence, adding eligible words to the `prime_words` list. Lastly, the function joins these prime words to form a string and returns the resulting string. 

The `is_prime` function utilizes a optimized checking mechanism to ascertain whether a number is prime or not. It initiates with iterative checking from 2 up to the square root of the number, and returns True if no divisors are found. If the number is less than or equal to 1, it is immediately labeled as not prime. 

The combined approach allows the given problem to be efficiently solved and tested.  This code can be executed directly in your Python environment to validate its functionality and is also compatible with various testing frameworks like `pytest` for comprehensive assessment. 
```python
# Test the is_prime function
assert is_prime(17) == True
assert is_prime(15) == False

# Test the words_in_sentence function
assert words_in_sentence("The quick brown fox") == "quick brown"
assert words_in_sentence("Hello World") == "Hello"
```