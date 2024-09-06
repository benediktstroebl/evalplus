Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split()  # Split the string into words on spaces
    result = [word for word in words if len(word) >= n and sum(1 for char in word if char in consonants) == n]
    return result if result else []

# Test cases
print(select_words("Mary had a little lamb", 3))  # Output: ['Mary', 'lamb']
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ['world']
print(select_words("Uncle sam", 3))  # Output: ['Uncle']
```

This script first defines a constant `consonants` that stores all consonants in English, both lowercase and uppercase. It then splits the input string `s` into a list of words using spaces as separators. The list `result` is then populated with words from `words` that have exactly `n` consonants, and finally, this list is returned if it is not empty, or an empty list is returned.