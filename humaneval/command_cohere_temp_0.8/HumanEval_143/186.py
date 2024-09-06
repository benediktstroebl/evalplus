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
        sentence (str): A sentence with spaces separating words

    Returns:
        str: A new sentence with words whose lengths are prime numbers
    """
    words = sentence.split()  # Split the sentence into words
    prime_words = []  # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a new sentence

# Test the function
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes a check for prime numbers using a predefined function called `is_prime`. The `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then constructs a new sentence from the prime-length words, all while maintaining the original order. 

Let's assume the `is_prime` function is defined correctly and does not have any logic issues. Feel free to test this code with other input sentences to verify the results!