Here is a Python script with a self-contained function that solves the problem:
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
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This script includes a function `is_prime`, which checks whether the given number is prime or not. The `words_in_sentence` function first splits the sentence into words using space as a delimiter. Then, it iterates over the words and checks their lengths using the `is_prime` function. If the length is prime, it includes the word in the `prime_words` list. Finally, it joins the prime words using a space as before to form the final answer.

Note: The `is_prime` function is used inside `words_in_sentence` and is not given any input in the provided prompt, but it is still part of a self-contained solution.  If you want to minimize the number of functions for a self-contained code block, you can instead use a one-liner `prime = set(range(2, len(sentence) + 2))` and check if the length of each word exists in the prime set.  This skips the need for a separate function for prime checking, but at the cost of more lines in the `words_in_sentence` function.  Please let me know if you would like me to provide this alternative solution.