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
    words = sentence.split()  # Split the sentence into words using space as delimiter
    prime_words = [word for word in words if is_prime(len(word))]  # Check the length of each word is prime or not
    return ' '.join(prime_words)  # Join prime words back into a string
```

This script includes the `is_prime` function for checking whether a given number is prime or not. The `words_in_sentence` function splits the input sentence into words, iterates through the words, and checks if the length of each word is prime, including it in the `prime_words` list if it is. Finally, the script joins the prime words back into a string and returns it. 

The `is_prime` and `words_in_sentence` functions are self-contained and can be called independently. 

This solution will work for the test cases mentioned in the prompt and produces the expected output, including the examples you provided.