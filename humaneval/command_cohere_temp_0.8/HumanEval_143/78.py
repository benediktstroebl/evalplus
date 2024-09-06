Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words with prime lengths in their original order.
    """
    words = sentence.split()  # Split the sentence into words using spaces as separators
    prime_words = []            # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a new sentence

# Test the function with a few inputs
print(words_in_sentence("Let's play a game"))  # Expected output: "Let's "
print(words_in_sentence("What is the meaning of life?"))  # Expected output: "Is"
```

This script includes a `is_prime` function for primality checking and the `words_in_sentence` function that solves the problem using the algorithm provided. The `is_prime` function checks whether a given number (in this case, the length of a word) is a prime number or not. The `words_in_sentence` function takes a sentence as input, splits it into words, and then checks the length of each word to see if it's prime. It collects the prime words in a list and then joins them back together to form a new sentence, preserving the original order.