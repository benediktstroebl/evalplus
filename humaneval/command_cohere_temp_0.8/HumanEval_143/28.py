```python
import math

def is_prime(n):
    """
    Checks whether the given integer is a prime number or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.
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

    Args:
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """
    words = sentence.split()  # Split the sentence into words using spaces
    prime_words = []           # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list if it's prime

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

The `is_prime` function is used to determine if a given number is prime or not. Then, the `words_in_sentence` function takes an input sentence, splits it into words using spaces, and then checks the length of each word, adding them to the `prime_words` list if their length is prime. Finally, the function joins the prime words back into a sentence, ensuring that only words with prime lengths are included, as described in the problem statement.