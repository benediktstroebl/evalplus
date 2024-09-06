```python
import math

def is_prime(n):
    """
    Checks whether the number is prime or not.
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
    """
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = []          # list to store prime words

    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the list if it's prime

    return ' '.join(prime_words)  # join the prime words to form a string
```

This script includes the `is_prime` function for checking if a number is prime, which is used here to determine if a word's length is prime.

The `words_in_sentence` function first splits the input sentence into individual words using spaces as separators. Then, it iterates through these words, checking their lengths with the `is_prime` function. If a word has a prime length, it's added to the `prime_words` list. Finally, the function joins the prime words back into a single string and returns the result.

The unit test is also included in this script:
```python
def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

    # Test with different characters in the sentence
    assert words_in_sentence("aaa bbb ccc ddd") == "bbb"
    assert words_in_sentence("123 abc 456 def") == "abc"

    # Test with uppercase letters and numbers
    assert words_in_sentence("Testing... 1... 2... 3...") == "Testing..."

test_words_in_sentence()
```

This should give you a complete solution to the problem statement.