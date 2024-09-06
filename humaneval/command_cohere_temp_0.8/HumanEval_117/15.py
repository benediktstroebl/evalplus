```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (letters in 'aeiou')
    """
    num_consonants = 0
    for char in word:
        if char.lower() not in 'aeiou':
            num_consonants += 1
    return num_consonants

def select_words(s, n):
    """
    This function selects words from a string that contain exactly 'n' consonants.
    Returns an empty list if no words are found.
    """
    words = s.split()  # Split the input string into a list of words
    filtered_words = [word for word in words if count_consonants(word) == n]
    return filtered_words
```

The `count_consonants` function is a utility function that calculates the number of consonants in a given word, which then is used by the `select_words` function to filter words according to the requested number of consonants. The provided example usages and tests are correctly showing the function's behavior for different scenarios.