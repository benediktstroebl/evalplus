Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
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
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = []          # list to store prime words
    for word in words:
        if len(word) > 1 and is_prime(len(word)):  # check if the length of the word is greater than 1 and is prime
            prime_words.append(word)
    return ' '.join(prime_words)  # join prime words to form a string

# Test Cases
print(words_in_sentence("This is a test"))  # Output: is
print(words_in_sentence("lets go for swimming"))  # Output: go for
```

This script will correctly identify and return a string containing only words whose lengths are prime numbers, with the order of words in the new string being the same as in the original sentence. 

Note: I replaced the `is_prime` function with a more efficient one that only checks up to `int(n**0.5) + 1`. And for large `n`, this approach is way more efficient than the previous one. 

The `is_prime` function is also included to check whether a given number is prime or not. 

This should address all the issues and provide a more efficient and effective solution.