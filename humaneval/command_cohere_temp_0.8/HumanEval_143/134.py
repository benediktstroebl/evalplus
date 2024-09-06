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
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This function `is_prime` is used to identify prime numbers. The function `words_in_sentence` takes a sentence as input, splits it into words using spaces as separators, and then iterates through each word. It checks the length of each word using the `is_prime` function and adds any prime-length words to the `result` string, ensuring that the order of words remains the same as in the original sentence.  The resulting string containing prime-length words is then returned.  It should be noted that the function `is_prime` is not necessarily optimized for speed and may not be suitable for very large numbers, but it is sufficient for the given problem constraints.  This approach ensures that the code is easily understandable and adheres to the problem guidelines.  Any variations or optimizations would be based on specific problem constraints and preferences for the code's elegance and efficiency.  Please let me know if you have any questions or need further refinement.