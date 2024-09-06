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
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]
```

This approach takes a sentence as input, first splits it into words using spaces as separators, then iterates through each word, and finally checks if the length of each word is a prime number, if it is, that word is added to a new string (`new_sentence`) with spaces in between to maintain the same order as in the original sentence, and this process is repeated for all words in the sentence, and the prime word subset is returned.