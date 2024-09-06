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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This approach divides the given sentence into words using `split()` method, then it checks the length of each word whether it is prime or not using the `is_prime()` function, and finally, it returns a string containing only the words whose lengths are prime numbers. 

The `is_prime()` function is implemented to iterate through the numbers from 2 to `sqrt(n)`, if there's no divisor found it returns `True`, else `False`.