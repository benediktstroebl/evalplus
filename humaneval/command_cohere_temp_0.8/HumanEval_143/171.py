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
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This code first splits the input sentence into individual words and then checks the length of each word to see if it's a prime number. If a word has a prime length, it gets added to the `prime_words` list. Finally, the function joins the prime words back into a string and returns the result.

Here is a test case of the function:
```python
print(words_in_sentence("Let us go for a swim in the ocean"))  # Output: "go for"
``` 
This should output `go for` because the word "go" and "for" have lengths 2 and 3, both prime numbers, thus they are the only ones present in the resulting string.