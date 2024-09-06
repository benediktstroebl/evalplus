Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(' ')
    res = []
    for word in words:
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)
```

This script includes a `is_prime` helper function to check if a number is prime or not. The main function `words_in_sentence` splits the sentence into words using whitespace as a delimiter, then it iterates through the words, checking the length of each word, and includes those whose length is a prime number in the `res` list. Then the final output is a string that joins all the prime-length words together with spaces, preserving the order of words from the original sentence.