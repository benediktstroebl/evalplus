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
        sentence (str): The input sentence with words separated by spaces

    Returns:
        str: A new sentence that contains words with prime lengths only
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This script includes a function `is_prime` that checks if a given number is prime or not. It also includes the `words_in_sentence` function that splits the sentence into words, checks the length of each word, and builds a new sentence from words with prime lengths. The `words_in_sentence` function solves the task as described in the prompt and the example cases.

This code would work as expected and solve the problem with the given input constraints. You can use it as a self-contained Python script to solve this specific problem.