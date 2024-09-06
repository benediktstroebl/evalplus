Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean value represents whether n is prime or not
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

    :param sentence: input sentence
    :return: string with words whose lengths are prime numbers
    """
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = []          # list to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # join prime words to form a string
```

This script includes the `is_prime` function for checking if a number is prime or not. The `words_in_sentence` function splits the input sentence into words, checks each word's length for primality, and then constructs a new string from the prime-length words, all while maintaining the original word order. 

The code should perform efficiently because the primality check is performed only for the lengths of words, which yields a maximum of 100 iterations (considering the given constraint of maximum sentence length of 100 characters). Thus, it would not pose any performance concerns for the provided constraints. 

This approach ensures that the prime words are collected correctly and efficiently, resulting in a structured and optimized solution.