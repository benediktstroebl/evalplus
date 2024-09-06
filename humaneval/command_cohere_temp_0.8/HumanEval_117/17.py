```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    consonants are all letters except a, e, i, o, and u
    """
    count = 0
    for char in word:
        if char not in 'aeiou':
            count += 1
    return count

def select_words(s, n):
    """
    This function takes a string s and an integer n, returning a list of all words from s that contain exactly n consonants.
    If the string is empty or the number is invalid, an empty list is returned.
    """
    if not s:
        return []
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is a utility function that calculates the number of consonants in any given word. 

The `select_words` takes a string `s` and an integer `n` as inputs and returns a list of words from the string `s` that contain exactly `n` consonants. The code first splits the string into words and then checks if each word contains `n` consonants using the `count_consonants` function.

The above code solves the problem as required in the prompt and also includes a useful utility function that can be used to count consonants in words. This makes the code more reusable and more understandable as the code is more self-explained.