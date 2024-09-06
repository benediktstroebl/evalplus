Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if prime or not.

    Returns:
        bool: If number is prime returns true, otherwise false.
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
        str: A string containing words with prime lengths.
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This script includes a check for prime numbers using a predefined function called `is_prime`. It also uses the `split` function to divide the sentence into individual words and then verifies the length of each word to see if it's prime. If a word has a prime length, it's added to a list called `prime_words`. Finally, the function joins these prime words back into a string and returns the result.

Let's break down the code and explain each part step by step:
1. **Function Definition:**
   ```python
   def is_prime(n):
       ...
   ```
   This part defines a function named `is_prime` that takes a single argument `n`, which is the number to be checked for primality. This function will determine whether `n` is a prime number or not and return a boolean value (`True` if prime, `False` otherwise).
2. **Prime Checking Logic:**
   ```python
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   ```
   This block of code is the core logic of the `is_prime` function. It employs an efficient algorithm known as the **Sieve of Eratosthenes** to check for prime numbers. Here's how it works:
   - `if n <= 1: return False`: If the number is less than or equal to 1, it's not prime, so the function returns `False`.
   - The loop starts from `i = 2` and goes up to the square root of `n`. If `i` exceeds the square root, the loop will handle that by adding 1 to the loop limit in the next iteration.
   - `if n % i == 0: return False`: The function checks if `n` is divisible evenly by `i`. If it is, then `n` is not prime, and the function returns `False`.
3. **Prime Word Search:**
   ```python
   def words_in_sentence(sentence):
       ...
   ```
   This part defines a new function named `words_in_sentence` that takes a sentence as input. This function splits the sentence into individual words using spaces as separators and then checks each word's length for primality.