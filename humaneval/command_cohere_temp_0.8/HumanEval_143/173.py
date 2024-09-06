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
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This script includes a separate function `is_prime` that checks if a given number is prime or not. The main function `words_in_sentence` splits the input sentence into words, checks if the length of each word is prime, and collects them in the `prime_words` list. Finally, it joins the prime words back into a string and returns the result.

The code above provides an efficient solution to the problem statement with a time complexity of O(N*log(N)) for checking the primality of each word length, where N is the total number of words in the sentence.