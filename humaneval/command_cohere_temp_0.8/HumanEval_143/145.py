Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

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
    words = sentence.split()
    primes = []
    for word in words:
        if is_prime(len(word)):
            primes.append(word)
    return ' '.join(primes)
```

This script includes a `is_prime` function to check if a number is prime or not. The `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then reconstructs a string from the prime-length-having words.

Note that this code assumes that the input sentence contains only letters and spaces, and that the length of the sentence is less than or equal to 100. You can adjust the code if you have different requirements or constraints.