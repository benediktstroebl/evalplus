Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
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
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)

# Test Cases
print(words_in_sentence("This is a test"))  # Should output: 'is'
print(words_in_sentence("lets go for swimming"))  # Should output: 'go for'
```

This script defines a function `words_in_sentence` that takes in a sentence as an input and returns a sentence with only the words whose lengths are prime numbers. It achieves this by first splitting the input sentence into individual words using spaces as separators. Then, it iterates through each word, checking if its length is prime using the `is_prime` function. If a word has a prime length, it's added to a list called `prime_words`. Finally, the function rejoins the words in `prime_words` to form a single sentence and returns it.

The script also includes a function `is_prime` that checks if a given number is prime or not, which is a reimplementation of the prime-checking algorithm. This function is used by `words_in_sentence` to determine if a word's length is prime.