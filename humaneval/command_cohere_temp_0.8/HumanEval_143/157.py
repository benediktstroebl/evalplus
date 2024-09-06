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
        sentence (str): Input sentence with spaces as delimiters.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

This function leverages the `is_prime` helper to check whether a number (in this case, the length of a word) is prime or not. It then filters the words whose lengths are prime numbers and returns them in the same order as in the original sentence.

You can verify the functionality with some test cases:
```python
# Test cases for the is_prime function
print(is_prime(4))  # Should print False
print(is_prime(5))  # Should print True

# Test cases for the words_in_sentence function
print(words_in_sentence("This is a test"))  # Should print "is"
print(words_in_sentence("lets go for swimming"))  # Should print "go for"
``` 

This approach ensures that the lengths of the words in the resulting sentence are prime numbers, while maintaining the original order of the words. 
If you have any questions, feel free to ask!