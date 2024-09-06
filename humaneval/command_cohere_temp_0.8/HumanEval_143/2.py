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
        sentence (str): Input sentence with spaces as delimiter.

    Returns:
        str: A sentence with words of prime lengths, keeping the original order.

    Example:
        Input: "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check word length for primality
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

This `is_prime` function is used to determine whether a number is prime or not. It iterates from 2 up to the square root of the number being checked, and checks if the number is divisible by any other number. If it is, then the number is not prime. If the number is not divisible by any number in this range, it is deemed prime. This approach provides an efficient primality check for larger numbers.

The `words_in_sentence` function first splits the input sentence into individual words using spaces as the delimiter. It then iterates through each word, checking its length for primality using the `is_prime` function. If the length is prime, the word is added to the `prime_words` list. Finally, the function joins the prime words back into a sentence using space as the delimiter, thereby producing a new sentence with words having prime lengths, while maintaining the original order.

This approach offers an efficient solution, as it checks each word's length for primality only once, contributing to a time complexity of O(n), where n is the number of words in the input sentence. The `is_prime` function ensures that the prime length check for each word is done optimally.