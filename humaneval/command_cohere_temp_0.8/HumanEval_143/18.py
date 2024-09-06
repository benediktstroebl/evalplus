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
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)

# Test the is_prime function
print(is_prime(17))  # Should print True
print(is_prime(16))  # Should print False

# Test the words_in_sentence function
print(words_in_sentence("This is a test"))  # Should print "is"
print(words_in_sentence("lets go for swimming"))  # Should print "go for"
```

This script includes a `is_prime` function to check whether a given number is prime or not, and the `words_in_sentence` function that extracts words from a sentence whose lengths are prime numbers. 

Both functions are equipped with docstrings to describe their purpose and behavior. You can use these functions independently for different scenarios where you need to verify primality or extract prime-length words from a given sentence. 

Feel free to adapt this solution according to your specific needs. If you have further questions or additional requirements, please don't hesitate to ask!