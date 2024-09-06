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
        sentence (str): Input sentence with spaces.

    Returns:
        str: Sentence with only words of prime lengths.
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result
```

This script includes a `is_prime` function for primality testing, which is useful for various mathematics-related tasks. The `words_in_sentence` function splits the input sentence into words using space separation, then iterates through the words to include only those with prime lengths, rejoining them in the original order.  It ensures the output includes only words with lengths that are prime numbers, providing a string representation that maintains word order while filtering based on the given constraint. 

This solution is designed to handle scenarios where you need to work with prime or composite numbers in a variety of contexts, such as number theory, cryptography, or algorithmic problems. It can potentially be optimized further, but it provides a solid foundation and incorporates primality testing, which is a crucial concept in number theory and applies to various practical applications in computer science and beyond. 

Below is a test for the function `words_in_sentence`:
```python
def test_words_in_sentence():
    sentences = [
        "This is a test",
        "An elephant is the largest animal in the safari. Lets go for swimming",
        "Time to crack some nuts!",
    ]
    
    expected_results = [
        "is",
        "go for",
        "Time"
    ]
    
    for sentence, expected in zip(sentences, expected_results):
        result = words_in_sentence(sentence)
        assert result == expected, f"For sentence '{sentence}'\n\nExpected: {expected}\nActual: {result}"
```
This test verifies the ability of the `words_in_sentence` function to extract words with prime lengths from an input sentence. Different test cases are provided to cover various scenarios, and the assert statements ensure that the function's behavior matches the expected output for each sentence.