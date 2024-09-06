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
        sentence (str): Input sentence with words separated by spaces

    Returns:
        str: A string containing words with prime lengths from the original sentence 
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This code defines a function `words_in_sentence()` that takes in a sentence and returns a modified sentence with only words whose lengths are prime numbers.

The prime number checking function `is_prime()` is also included in the code and is used to check if a given number is prime or not. 

Note: For the code to work, there should be a test suite with corresponding test cases to cover different edge scenarios to ensure that the code behaves as expected.