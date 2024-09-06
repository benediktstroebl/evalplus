Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
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
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()

# Test Cases
assert words_in_sentence("This is a test") == "is"

assert words_in_sentence("lets go for swimming") == "go for"
```

This script includes a `is_prime` helper function to check if a number is prime. The `words_in_sentence` function splits the sentence into words, iterates through the words, and appends the words whose length is a prime number to the `result` variable. Finally, it returns the `result` string.

The code includes unit tests to ensure the `words_in_sentence` function behaves as expected. You can use these tests to check that the code operates correctly. 

You can use the `is_prime` function independently to check whether an integer is a prime number.