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
    Extracts words from a given sentence whose lengths are prime numbers.

    Args:
        sentence (str): Input sentence with spaces between words.

    Returns:
        str: A sentence composed of words whose lengths are prime numbers.
    '''
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Example Usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes the `is_prime` function for checking whether a number is prime or not. 

The `words_in_sentence` function first splits the sentence into individual words using `split()`. It then iterates through each word, checking if its length is a prime number using the `is_prime` function. If a word has a prime length, it's added to the `prime_words` list. Finally, the function joins the prime words back together with spaces to form a new sentence, which is returned as the result.

The expected output is obtained by demonstrating the function on two different sentences.