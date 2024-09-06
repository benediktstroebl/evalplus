```python
import math

def is_prime(n):
    """
    Checks whether a number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Extracts words from a sentence with prime lengths.

    Args:
        sentence (str): Input sentence with spaces as delimiter.

    Returns:
        str: A sentence with words of prime lengths.
    """
    words = sentence.split()  # Split sentence into words using spaces
    prime_words = []          # List to store prime words

    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add prime word to the list

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

This function leverages a primality testing mechanism to identify words within the provided sentence that possess prime lengths. It then constructs a new sentence from these prime-length words, preserving the original sentence's word order.

Here is an example of how you can use the `words_in_sentence` function to solve the problem:
```python
# Example 1
input_sentence = "This is a test"
print(words_in_sentence(input_sentence))  # Output: "is"

# Example 2
input_sentence = "lets go for swimming"
print(words_in_sentence(input_sentence))  # Output: "go for"
```

This script ensures the function's effectiveness in extracting words with prime lengths from a given sentence, providing a concise and self-contained solution to the problem.