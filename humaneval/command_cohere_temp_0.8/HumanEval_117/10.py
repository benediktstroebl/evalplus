```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            total += 1
    return total

def select_words(s, n):
    """
    Given a string s and a natural number n, return a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    A word contains consonants if it has at least one consonant and contains at least one vowel.
    """
    if not s:
        return []

    words = s.split()
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count > 0 and len(word) - consonant_count > 0:
            if consonant_count == n:
                result.append(word)

    return result
```

The approach employs a helper function, `count_consonants`, to tally the number of consonants in a word. Then, for each word in the string split by spaces, the function examines whether it contains both consonants and vowels, and if so, adds it to the result list if it contains precisely n consonants. Lastly, the function returns this list. 

Note: this solution assumes only letter characters and spaces in the input string.