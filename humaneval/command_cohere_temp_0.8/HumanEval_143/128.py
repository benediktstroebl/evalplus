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
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This function `is_prime` checks if a number is prime or not, and `words_in_sentence` uses it to filter words from the given sentence that have prime lengths. The solution avoids adding additional complexity by removing punctuation or dealing with spaces, sticking to the specified constraints.

Here is how you can use the above function to solve the given problem:
```python
print(words_in_sentence("This is a test"))  # Output: 'is'
print(words_in_sentence("lets go for swimming"))  # Output: 'go for'
```

This minimalist approach aligns with the given constraints, providing a straightforward solution without introducing unnecessary complexity.  If desired, we can add further robustness with upper/lowercase handling or additional primality tests. Let me know if you want to pursue any specific enhancements, and I'll be glad to assist further.