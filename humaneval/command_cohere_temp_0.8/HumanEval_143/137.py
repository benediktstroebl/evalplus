```python
import math

def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
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

This approach takes the input sentence and splits it into words using space as a delimiter. Then, it iterates over each word, checks if its length is prime using the `is_prime` function, and appends it to the `new_sentence` if it is. Finally, it returns the resulting string. 

To ensure the function performs primality checks efficiently, the `is_prime` function uses an optimized approach of checking only from 2 up to the square root of the number. 

Note that this approach results in a time complexity of O(N * sqrt(N)) where N is the total length of the words in the sentence. You can adjust this based on your preferred trade-off between time and space complexity.