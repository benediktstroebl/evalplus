Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
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

# Test Cases
print(words_in_sentence("This is a test"))  # Should output: 'is'
print(words_in_sentence("lets go for swimming"))  # Should output: 'go for'
```

This script will correctly identify and return a string containing the words from the input sentence that have lengths which are prime numbers.

Let's break down the code:
1. `is_prime(n)`: This function checks whether the given number `n` is prime or not. It does this by iterating from 2 to the square root of `n`, if `n` is divisible by any of these numbers, it returns `False`. If it isn't, it returns `True`.
2. `words_in_sentence(sentence)`: This function takes a sentence as input, splits it into words (assuming words are separated by spaces), and then checks the length of each word to see if it's prime. If a word has a prime length, it's added to the `result` list. Finally, the function joins the `result` list back into a string and returns it. 

This solution is efficient as the prime checking function `is_prime(n)` uses an optimized approach to check for prime numbers within the range of [2, n**0.5] which is the range of possible divisors for a given number `n` with a linear time complexity of O(n**.5).