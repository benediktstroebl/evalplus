Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This script includes a separate function `is_prime(n)` that checks if a number is prime or not. The main function `words_in_sentence()` splits the input sentence into words, iterates through them, and checks their lengths with the `is_prime()` function. If the length of a word is prime, it's added to the `result` list, and then the function joins the list of prime words to form a string and returns it.

Ensure you have the `split()` method which splits the string into a list of strings based on spaces, the `is_prime()` function which checks if a number is prime, and the `join()` method which joins the elements of a list into a single string. These methods and functionalities are provided within the Python language itself, so you don't need to install any additional modules. 

This approach ensures that the function is self-contained and doesn't rely on any external libraries other than the Python standard library.