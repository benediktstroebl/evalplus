Here is a Python script with a self-contained function that solves the problem:
```python
import math

def is_prime(n):
    """
    Checks whether the number 'n' is prime or not.
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
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```
The `is_prime` function checks if a number is prime or not. The `words_in_sentence` function splits the input sentence into words and then iterates through the words. It checks if the length of each word is prime using the `is_prime` function, and if so, it adds the word to the `new_sentence` string, with a space as a delimiter. The final result is returned after removing the last trailing space to avoid any extra whitespace. 
This solution works smoothly for problems like this, as the constraint states that the sentence contains only letters. 
The code also includes an additional test to cover different cases. You can use it by adding a test case in the `__main__` section at the end of the script:
```python
# Description: Testing the function
def test_words_in_sentence():
    sentence = "This is a test"
    expected = "is"
    result = words_in_sentence(sentence)
    assert result == expected

# Run the test
test_words_in_sentence()
```
Make sure to have an accurate description of the test case to facilitate its interpretation.