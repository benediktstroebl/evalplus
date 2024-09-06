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
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words whose lengths are prime numbers.
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result

# Example Usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes a separate function `is_prime` that checks if a number is prime or not. The main function `words_in_sentence` splits the sentence into words, and then iterates through the words, checking if their length is prime with the help of the `is_prime` function. If a word has a prime length, it is added to the `result` string, with the order maintained from the original sentence.