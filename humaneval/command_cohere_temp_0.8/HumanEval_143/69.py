Here is a Python script with a self-contained function that solves the problem:
```python
import math

def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Extracts words from the sentence whose lengths are prime numbers.

    Args:
        sentence (str): Input sentence to process.

    Returns:
        str: A string containing only words with prime lengths, in the same order as the input sentence.

    Usage:
        >>> words_in_sentence("This is a test")
        'is'
        >>> words_in_sentence("lets go for swimming")
        'go for'
    """
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = []            # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)
    
    return ' '.join(prime_words)  # Join prime words to form a string
```

The `is_prime` function is used to determine if a given number is prime. It does so by iterating from 2 up to the square root of the number being checked, and verifying if the number is divisible by any of these integers. If a number is not divisible by any of these integers, it is deemed prime. This function forms the basis for our primality check. 

The `words_in_sentence` function takes an input sentence and splits it into individual words using spaces as separators. It then iterates through each word, checking the length of each word using the `is_prime` function. If a word has a prime length, it is added to the `prime_words` list. Finally, the function joins the prime words back into a string and returns it.

You can use the `words_in_sentence` function by passing a sentence as an argument. It will return a string containing only the words with prime lengths, arranged in the same order as they appeared in the original sentence. 

This solution works for sentences with a maximum length of 100 characters and only contain letters, as stated in the prompt's constraints.