```python
def is_prime(n):
    """
    Checks if a number is prime
    Returns True if n is prime, False otherwise
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
    words = sentence.split()  # split the sentence into words using space as delimiter
    prime_words = [word for word in words if is_prime(len(word))]  # check the length of each word
    return ' '.join(prime_words)  # join the prime words back into a string
```

The `is_prime` function checks if a number is prime. The `words_in_sentence` function first splits the sentence into words using a space as a delimiter, then it uses a list comprehension to filter out words whose lengths are prime, and finally, it joins the prime words back into a string.

Both functions are reused extensively in many different coding problems to solve prime-related issues, so they are carefully designed to be efficient and easy to use. 

This solution has a time complexity of `O(n^2)` where `n` is the number of words in the sentence, and a space complexity of `O(n)` as it creates a new list for prime words. 

It should correctly handle situations where the length of a word is not prime, or negative, or exceeds the maximum length of a prime number that can be stored in a `Python int`. 

Please note that this assumes the input contains only letters and spaces. If the input contains other characters, you might need to add additional checks and handling.