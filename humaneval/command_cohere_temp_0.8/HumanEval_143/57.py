Here is a Python script with a self-contained function that solves the problem:
```python
import math

def is_prime(n):
    """
    Checks whether the given integer is a prime number or not.

    Args:
        n (int): Integer to check for primality.

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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()  # Split the sentence into words using spaces as separators
    prime_words = []          # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words
    
    return ' '.join(prime_words)  # Join prime words to form a single string and return

# Test the function
sentence1 = "This is a test"
print(words_in_sentence(sentence1))  # Output: "is"

sentence2 = "lets go for swimming"
print(words_in_sentence(sentence2))  # Output: "go for"
```

This script includes a `is_prime` function to check if a given integer is a prime number or not. The `words_in_sentence` function then splits the sentence into words, checks their lengths for primality, and returns a string containing only the words with prime lengths, in the original order. The `Example1` and `Example2` are handled to validate the functionality of the script.

Note that this approach has a time complexity of O(k*log(k)), where k is the number of prime words, which can be quite efficient for a large input size. You can also optimize it further using the Sieve of Eratosthenes algorithm to further improve the time complexity, reducing it to O(k*log(log(k))). If the input size is small, the difference between the two won't be noticeable, but for larger inputs, the optimized version might perform better.