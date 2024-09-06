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
    words = sentence.split()  # split the sentence into words according to space
    prime_words = []  # a list to store prime words
    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the list if it's prime
    return ' '.join(prime_words)  # join the prime words to a string and return
```
The `is_prime` function checks if a number is prime or not. The `words_in_sentence` function first splits the sentence into words according to the spaces, then it checks each word's length against primality using `is_prime`, and finally, it returns a string consisting of the words whose lengths are prime numbers, concatenated together with spaces in the same order as they appeared in the original sentence.

This solution works for sentences with lengths [1,100] and contains only letters (uppercase and lowercase). It provides the required prime-length words in the output. 
The code covers primality checking and handles the constraints of the problem nicely. 

Note: this code uses `math.sqrt` for a square root operation, which is efficient, and the square root is always positive, so there is no need to worry about negative inputs. In typical scenarios where you need only a limited number of prime checks, the code provides an efficient and readable solution. However, if you need millions of prime checks, using a specialized library like 'prime' would be more efficient.  Also, the code is case-sensitive, so it might behave differently with capitalized sentences. You may want to consider making the input case-insensitive depending on your use case.  If you are unsure, it is always helpful to provide the expected input and output format based on the given constraints to facilitate code evaluation.  Feel free to re-submit the question with additional details, and I'll be glad to assist!