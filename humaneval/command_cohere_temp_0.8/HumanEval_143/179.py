Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if prime or not.

    Returns:
        bool: If number is prime returns True, otherwise False.
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

This script includes a `is_prime` function to check if a number is prime or not. The `words_in_sentence` function splits the input sentence into words, checks for each word if its length is prime, and then returns the words with prime lengths, joined together into a string.

The `is_prime` function is used to check if a number is prime or not. It takes in an integer `n` as an argument, and returns a boolean value of True if the number is prime, and False otherwise. The function uses a simple algorithm to check for primality, which is based on checking if any number between 2 and the square root of the number is a divisor of the number or not. If any such divisor is found, the function returns False, otherwise, it returns True. 

The `words_in_sentence` function is the main function that is responsible for solving the problem. It takes in a string `sentence` as an argument, and returns a string containing the words from the original sentence whose lengths are prime numbers. The order of the words in the new string is the same as the original one. 

The function first splits the sentence into words using the `split` method. Then, it initializes an empty list `prime_words` to store the prime words. Then, iterates over each word in the sentence, and checks if the length of the word is prime using the `is_prime` function. If the length of the word is prime, it appends the word to the list `prime_words`. Finally, the function returns a string containing the words in `prime_words`, joined together with a space character between them. 

You can use these functions with the following snippet of code to test them:
 ```python
print(words_in_sentence("Let's go for swimming")) # Output: "go for"
print(is_prime(41)) # Output: True
``` 

This should print:
```
go for
True
```