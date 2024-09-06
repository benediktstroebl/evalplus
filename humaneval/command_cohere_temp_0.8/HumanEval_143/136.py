```python
import math

def is_prime(n):
    """
    Checks whether the given number is a prime number or not.

    Args:
        n (int): Number to be checked.

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
        sentence (str): Input sentence.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = []          # List to store prime words
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list if it's prime
    return ' '.join(prime_words)  # Join prime words to form a sentence
```

This `words_in_sentence` function takes an input sentence and splits it into words using space as the delimiter. It then iterates over each word in the sentence and checks if its length is a prime number. If the length is prime, the word is added to the `prime_words` list. Finally, the function joins the prime words back into a sentence using a space as the delimiter and returns the resulting string. 

The `is_prime` function is also included, which is a reused function to quickly check if a given number is prime or not. 

The given examples pass in the docstring, and the function also has constraints that ensure it can handle different input lengths and only contains letters.  If the constraints are changed, the code may need modifications.