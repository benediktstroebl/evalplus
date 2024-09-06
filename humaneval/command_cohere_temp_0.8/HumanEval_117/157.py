```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split() if word]
    return [word for word in words if count_consonants(word) == n]

# Test Cases
print(select_words("Mary had a little lamb", 4))  # Output: ['little']
print(select_words("Mary had a little lamb", 3))  # Output: ['Mary', 'lamb']
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ['world']
print(select_words("Uncle sam", 3))  # Output: ['Uncle']
```

This Python script divides the task into two functions:
1. The `count_consonants` function calculates the number of consonants in a given word, determining if it matches the required count.
2. The `select_words` function first splits the input string into individual words and then filters them based on the consonant count requirements.

The script includes test cases to validate the function behaviors for various scenarios. Adjustments might be required when applying this code to different markdown formats. If there is any specific formatting requirement, feel free to clarify that.