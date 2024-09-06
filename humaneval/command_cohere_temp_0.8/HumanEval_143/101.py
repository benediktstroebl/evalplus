Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if prime or not.

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
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with spaces.

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
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

# Unit Test
sentence = "This is a test"
assert words_in_sentence(sentence) == "is"

sentence = "lets go for swimming"
assert words_in_sentence(sentence) == "go for"
```

This script includes a function called `words_in_sentence` that takes in a sentence as an argument and returns a string consisting of words whose lengths are prime numbers.

The prime number checking function `is_prime` is also included, which checks whether a given number is prime or not. The `words_in_sentence` function splits the sentence into words using spaces as separators, and then it iterates through the words, checking their lengths with the `is_prime` function. If a word has a length that is prime, it is added to a list that is later joined together to form the final output string.

The unit tests provided assert that the function `words_in_sentence` behaves as expected, and the tests are successfully passed. You can use this code to solve the problem you described efficiently and accurately. 

I hope this helps, let me know if there is anything else I can contribute!