```python
def is_prime(n):
    """
    Checks whether the integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Check the length of each word if it is prime
    return ' '.join(prime_words)  # join the prime words back into a string
```

The `is_prime` function checks if a given number n is a prime number or not. The `words_in_sentence` function splits the sentence into words, then loops through the words, checking the length of each word with the `is_prime` function, finally, it joins the prime words back into a string and returns it.

This solution works efficiently and meets the constraints of the problem, thus, passing the given tests.