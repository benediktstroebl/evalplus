Here's a Python script that solves the problem:
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
    for i in range(2, int(n ** 0.5) + 1):
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
        str: A sentence where only words with prime lengths are retained.
    """
    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)
```

This script defines a function `words_in_sentence()` that takes in a sentence and returns a modified sentence where only words with prime lengths are included.

The script also defines an auxiliary function `is_prime()` that checks if a given number is prime or not. This function is used in the `words_in_sentence()` to check if the length of each word in the sentence is prime. 

The `words_in_sentence()` function first splits the input sentence into individual words using space as a delimiter. It then initializes an empty list `prime_words` to store the prime words. Next, it iterates over each word in the sentence, calling the `is_prime()` function to check its length. If the length is prime, the word is added to the `prime_words` list. Finally, the function joins the prime words back into a single string to form the desired output sentence.