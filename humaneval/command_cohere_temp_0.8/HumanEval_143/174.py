Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
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
    """
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```
The function `words_in_sentence()` takes a sentence as input and returns a string containing the words whose lengths are prime numbers. This is done by first splitting the sentence into words using space as a delimiter, then iterating over the words, and checking if the length of each word is prime. If it is prime, the word is added to the new_sentence string, and finally, the function returns the new_sentence string.

Here's an example usage of this function:
```python
print(words_in_sentence("Let's go for swimming")) # Output: "go for"
```
This will be the output as the word 'go' and 'for' are prime numbers in length.