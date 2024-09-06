Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the number 'n' is prime or not.
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

# Testing the function
sentence = "This is a test"
print(words_in_sentence(sentence))  # Expected output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Expected output: "go for"
```

This script includes the `is_prime` function for checking whether a number is prime or not. The main function `words_in_sentence` splits the input sentence into words, checks the length of each word, and builds a list of prime-length words. Finally, it joins these prime-length words back into a string and returns the result.