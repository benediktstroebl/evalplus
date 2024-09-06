Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the integer 'n' is prime or not.

    Args:
        n (int): Integer to be checked.

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
        sentence (str): A string representing a sentence with space-separated words.

    Returns:
        str: A new sentence with words of prime lengths.

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
expected = "is"
print(f"For the sentence: '{sentence}', expected output: '{expected}'")
print(words_in_sentence(sentence) == expected)

sentence2 = "lets go for swimming"
expected2 = "go for"
print(f"For the sentence: '{sentence2}', expected output: '{expected2}'")
print(words_in_sentence(sentence2) == expected2)
```

This script includes a function called `words_in_sentence` that takes a sentence as input and returns a modified sentence with only words whose lengths are prime numbers.

It also includes a helper function called `is_prime`, which checks whether a given integer is a prime number or not. This function is essential for the `words_in_sentence` function to validate the lengths of words.

For better testing, the script provides sample inputs and expected outputs, along with print statements that compare actual vs. expected outputs.