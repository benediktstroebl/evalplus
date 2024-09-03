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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This code first splits the input sentence into individual words based on the space character. Then, it iterates through each word, checking if its length is a prime number using the `is_prime` helper function. If the length is prime, the word is added to the `result` list. Finally, the function joins the prime words back into a single string and returns the result.

Here's an example usage of the code:
```python
print(words_in_sentence("Let's go for swimming"))  # Output: "go for"
``` 
It will return the words "go" and "for", as their lengths (2, 4) are both prime numbers.