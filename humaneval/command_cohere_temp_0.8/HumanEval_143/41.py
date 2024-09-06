Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the number 'n' is prime or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if n is a prime number, False otherwise.
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
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

# Unit tests:
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True

def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence(" ailabless") == "ailabless"

test_is_prime()
test_words_in_sentence()
```

This script includes the `is_prime` function to check if a given number is prime or not. Then, the `words_in_sentence` function takes an input sentence, splits it into words separated by spaces, and checks the length of each word. If the length is prime, it includes that word in the `result` list. Finally, the function joins the `result` list to form a new sentence, which is then returned.

The code also includes unit tests for both the `is_prime` and `words_in_sentence` functions to ensure they behave as expected. You can run these tests by themselves to verify the correctness of the code.  You can do it by copying this code into a Python file (e.g., `prime_words.py`) and executing the file in your Python environment. 

To run the tests, you can use the `python prime_words.py` command in your terminal, and the script will run the tests and display whether they pass or fail. 

If you are using an IDE, you can create a test file (e.g., `tests.py`) and copy the tests there, then run the tests directly from your IDE.  This way, you can ensure the correct functionality of the code and verify that