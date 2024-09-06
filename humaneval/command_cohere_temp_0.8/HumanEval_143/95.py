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
        str: A sentence with words of prime lengths, kept in the original order.

    Example Usage:
        >>> words_in_sentence("Let's play chess!")
        'let play'
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

This function utilizes a `is_prime` function to determine if a number is prime. It then checks the length of each word in the sentence to see if it's prime, and collects these prime word lengths into a list. Finally, the function joins these prime words together to form a new sentence. The `is_prime` function is implemented as:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
``` 

This approach ensures that the resulting sentence contains only words with lengths that are prime numbers, and the words are arranged in the same order as they appeared in the original sentence. 
To ensure efficiency, the `is_prime` function utilizes an optimized approach by checking only up to the square root of `n`, rather than iterating through all numbers up to `n`. 

Note: The prime checking function (`is_prime`) has an O(sqrt(n)) time complexity, and the main function has an overall O(n) time complexity, where n is the length of the input sentence. 

This approach balances accuracy and efficiency, as the sqrt(n) factor in the `is_prime` function improves the time complexity compared to a naive linear search. 

The main function, `words_in_sentence`, iterates through the words in the sentence once and performs a constant-time operation to check for primality, resulting in an overall O(n) time complexity.