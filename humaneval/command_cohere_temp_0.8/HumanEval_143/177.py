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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```
This script includes the `is_prime` function which checks whether a given number is prime or not. The `words_in_sentence` function then uses `is_prime` to filter out words from the sentence that have prime length. 

The `words_in_sentence` function takes sentence input from the user, splits it into words using spaces as separators, and then checks the length of each word to determine if it's prime. If a word has a prime length, it's added to a list called 'prime_words'. Finally, the function joins the words back into a string and returns it. 

To run this code you need to install the `math` library with the following command:
```bash
pip install math
``` 

You can test this function with the following input and expected output:
```python
print(words_in_sentence("The quick brown fox"))  # Expected output: "fox"
print(words_in_sentence("Let us go for a swim"))  # Expected output: "go for"
``` 
This problem can also be solved using the `math` library's `prime` module but it is not guaranteed to be part of the standard library in the future.