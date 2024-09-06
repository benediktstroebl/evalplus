Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the number 'n' is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
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
    """
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```

This script defines a function `words_in_sentence` that accepts a string of text and identifies individual words using spaces as separators. It then checks the length of each word to see if it's a prime number, adding those prime-length words to a new string while maintaining their original order. The final output is the new string, excluding the last space.

Note: The `is_prime` function is included to verify whether a given number is a prime or not. It iterates through numbers from 2 to the square root of the input number, if it finds any divisor, it returns `False`, otherwise, it confirms the number is prime and returns `True`.