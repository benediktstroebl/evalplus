Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the integer 'n' is a prime number or not.

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
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
        sentence (str): The input sentence with spaces separating words

    Returns:
        str: A new sentence with words whose lengths are prime numbers

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    words = sentence.split(' ')
    result = ''
    for word in words:
        if is_prime(len(word)):
            result += word + ' '
    return result[:-1]
```

This script includes a separate function `is_prime` that checks if a number is prime or not. The main function `words_in_sentence` splits the input sentence into words, and then iterates through the words, checking their lengths with the `is_prime` function. If the length of a word is prime, it is added to the `result` string, with empty spaces preserving the original word order. Finally, this last string is returned.