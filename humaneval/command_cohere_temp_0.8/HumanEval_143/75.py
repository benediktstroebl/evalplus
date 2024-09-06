Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if prime or not.

    Returns:
        bool: If the number is prime or not.
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
        str: A new sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)
```

This script includes two functions:
1. The `is_prime` function checks whether a given number is prime or not.
2. The `words_in_sentence` function accepts a sentence and returns a modified sentence that only includes words with lengths that are prime numbers.

Note that this script assumes that the sentence provided only contains letters, and spaces and is less than or equal to 100 in length. And, the `is_prime` function iterates through numbers from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer in that range, it's not a prime number.