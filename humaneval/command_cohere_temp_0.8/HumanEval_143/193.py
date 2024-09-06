```python
import math

def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return " ".join(prime_words)
```

This code defines a function `words_in_sentence()` that takes a sentence as input, splits it into words separated by spaces, and then checks the length of each word to see if it's prime. If a word has a prime length, it's added to a list of prime words. Finally, the function joins the prime words back into a string and returns the result.

Here is an example usage of the function:
```python
print(words_in_sentence("Let's go for swimming"))  # Output: "go for"
``` 

This will output "go for" because the word "go" and the space between "go" and "for" have prime lengths.