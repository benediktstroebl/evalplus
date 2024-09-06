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
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): A sentence with spaces separating words.

    Returns:
        str: A subsequence of the original sentence containing only words with prime lengths.
    """
    words = sentence.split()  # Split the sentence into a list of words
    prime_words = []  # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the current word is prime
            prime_words.append(word)  # Add the word to the list of prime words

    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

This function leverages a primality testing method and iterates through each word in the provided sentence to identify those whose lengths are prime numbers. It then assembles these prime-length words to form a new sentence. 

Assuming you want to execute this script while showcasing its usage within the same file, you can continue providing the script with test scenarios. You can also incorporate it with unit tests if you aim to create a more organized and comprehensive file. Here's an illustration of how you can enhance the script with test scenarios to demonstrate its functionality:
```python
# ... (previous code with function definition) ...

def test_words_in_sentence():
    """
    Tests the correctness of the words_in_sentence function.
    """
    sentence = "This is a test with varying word lengths, and it handles punctuation."
    
    expected_result = "is a test with varying"
    assert words_in_sentence(sentence) == expected_result

    sentence = "lets go for swimming"
    expected_result = "go for"
    assert words_in_sentence(sentence) == expected_result

    sentence = "this is a sentence with a very long word that just fits primality criteria"
    expected_result = "a sentence with a very long"
    assert words_in_sentence(sentence) == expected_result

# Run the tests
test_words_in_sentence()

```

This way, the script is entirely self-contained, defines the function, and incorporates tests to showcase its practical usage. 
You can add more tests to cover a broader range of scenarios and ensure the function's correctness for various input conditions.