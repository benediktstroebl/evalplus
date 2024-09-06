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
This script splits the input sentence into words using space (' ') as a delimiter, then it iterates through the words, and if the length of a word is prime, it's added to the new_sentence string, and finally the last character (' ') is removed from the new_sentence to remove the extra space carried from the last word.

Note that the `is_prime` function is included to check if a number is prime or not, it takes care of the edge cases where the number is less than or equal to 1, and where the number is divisible by any number from 2 to its square root.

You can use this code to solve the problem stated in the Markdown block. You can test this function using different inputs to see which words with prime lengths are extracted.