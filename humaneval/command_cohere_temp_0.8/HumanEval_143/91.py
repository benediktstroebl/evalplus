Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the integer is a prime or not.
    :param n: Integer to check whether it is prime or not.
    :return: True if n is a prime, else False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```

This script defines a function `words_in_sentence` that takes a sentence as input and returns a modified sentence with only words whose lengths are prime numbers.

The script also includes a separate function `is_prime` to check if a given number is prime or not. This function is used in the `words_in_sentence` function to determine whether the length of each word is prime.

You can use this code to solve the problem you described, and it should pass any tests that are designed to verify this problem.