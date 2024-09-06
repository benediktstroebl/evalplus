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
        str: A string containing words with prime lengths in their original order.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This Python script includes a `is_prime` function to check whether a number is prime or not, which is a crucial step in solving the problem. The `words_in_sentence` function then splits the input sentence into words using space as a delimiter, and subsequently iterates through the words to check their lengths for primality. Words with prime lengths are concatenated together to form the final output, with the same order as in the original sentence. The code is encapsulated within a self-contained function, making it easily testable and reusable.