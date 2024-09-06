Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the integer `n` is a prime number or not.

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
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)
```

This script includes the `is_prime` function which checks if a given number is prime or not. The `words_in_sentence` function then uses `is_prime` to filter out words from the sentence that have prime lengths.

The `words_in_sentence` function takes a sentence as input and returns a string containing only the words whose lengths are prime numbers. It also maintains the order of the words in the new string to be the same as in the original sentence. 

You can use these functions with the provided explanations and the given test cases to solve the problem. Let me know if you have any questions!