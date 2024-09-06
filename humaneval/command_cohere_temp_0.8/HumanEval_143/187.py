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

This script defines a function `words_in_sentence` that takes a sentence as input and returns a modified sentence with only words whose lengths are prime numbers.

The script also includes a function `is_prime` to check if a number is prime or not. This function is used by `words_in_sentence` to determine whether a word's length is prime.

It then uses these functions to solve the problem and returns the modified sentence.

You can use this code to solve the problem you've described, and it should work as expected. 

I hope this helps! Let me know if you have any further questions or if you'd like to discuss more details.