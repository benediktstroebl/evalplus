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
    words = sentence.split()  # Split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Check the length of each word is prime or not
    return ' '.join(prime_words)  # Join prime words back into a string
```

This Python script defines a function `words_in_sentence` that accepts a sentence as input and returns a revised sentence containing only words whose lengths are prime numbers.

The script also includes an auxiliary function, `is_prime`, which checks whether a given number (in this case, the length of a word) is a prime number or not. This function is invoked within the `words_in_sentence` function to determine which words meet the prime-length criterion.

The approach fundamentally involves:
1. Splitting the sentence into individual words using spaces as separators.
2. Iterating through each word in the sentence, checking its length to determine if it's a prime number.
3. Lastly, the script rejoins the 'prime' words to form a new sentence, ensuring the word order remains unchanged from the original input. 

This solution will correctly identify and return a sentence comprised of words whose lengths are prime, while maintaining the original word order.