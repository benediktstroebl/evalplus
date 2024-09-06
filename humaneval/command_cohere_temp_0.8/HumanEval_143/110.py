Here is a Python script with a self-contained function that solves the problem:
```python
import math
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
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

    :param sentence: input sentence
    :return: string containing words with prime lengths
    """
    words = sentence.split()  # split the sentence into array of words
    prime_words = []          # container for prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)

# Test Cases
print(words_in_sentence("Let us go for a swim in the ocean"))
print(words_in_sentence("This is a test with varying lengths"))
```

The `is_prime` function checks if a number is prime or not, and the `words_in_sentence` function splits the sentence into words, checks for prime word lengths, and then returns the words with prime lengths, preserving the order. You can test this code with various input sentences to see which words have prime lengths. 
 every day!