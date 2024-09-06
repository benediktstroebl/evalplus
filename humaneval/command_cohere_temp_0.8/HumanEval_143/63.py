Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the integer is a prime or not.
    :param n: Integer to be checked
    :return: True if n is a prime, otherwise false
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
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This script includes a check for prime numbers using a predefined function called `is_prime`. The `words_in_sentence` function splits the input sentence into words using space as a delimiter, then it checks each word's length for primality, including the word in the `result` list if the length is prime, and finally joins the list of result words back into a string to return as the answer.

Note that this code assumes that the sentence contains only letters and spaces, and that each word is represented as a single string with no spaces within.