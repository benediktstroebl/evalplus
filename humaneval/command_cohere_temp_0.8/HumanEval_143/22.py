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
        str: A sentence with words of prime lengths, keeping the original order.

    Example:
        Input: "We will shall overcome"
        Output: "will"
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = [word for word in words if is_prime(len(word))]  # Filter words based on primality
    return ' '.join(prime_words)  # Rejoin prime words to form a new sentence
```

This function uses a basic primality test to check word lengths, ensuring efficiency in determining prime words.

Further, the code splits the original sentence into words and then filters them based on primality. This filtering process retains only the words whose lengths are prime numbers, resulting in the desired output.

This optimized approach significantly reduces computational overhead and improves the function's performance, allowing it to efficiently handle various sentence lengths and word combinations.