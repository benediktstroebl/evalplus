Here's a Python script that solves the given problem with an example:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: Number to be checked.
    :return: True if n is a prime number, else False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split() 
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

To use this script, you can define the function `is_prime(n)` which checks whether the number `n` is prime or not. Then, the function `words_in_sentence()` takes a sentence as input, splits it into words, and then checks the length of each word to see if its length is prime. If so, it includes that word in the `result` list in its original order. Finally, the function returns a string that contains the words that have prime lengths, concatenated together with a space as the separator.

This solution handles the constraints mentioned in the prompt and should produce the correct answer for the given test cases.