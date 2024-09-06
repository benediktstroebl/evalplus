```python
import math

def is_prime(n):
    """
    Checks whether the given integer is a prime number
    Returns true if n is greater than 1 and is a prime number, else false.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
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
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This approach splits the sentence into words using `split(' ')`, initializes an empty list `result` to store the prime-length words, and then iterates over each word in the sentence using a for loop. Using the `is_prime` function, it checks if the length of each word is a prime number, and if so, it's added to the `result` list. Finally, the function joins the prime-length words back into a string using ' '.join(result) and returns it.

The `is_prime` function is included to ensure the logic works correctly for checking prime numbers.