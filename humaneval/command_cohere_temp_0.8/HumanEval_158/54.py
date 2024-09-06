```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] > len(char_count):
            max_char_word = word
    if max_char_word is None:
        return ""
    return max(max_char_word, key=lambda x: (char_count[x], x))
```

The code defines a function `find_max` that takes in a list of words and returns the word with the highest count of unique characters, using a dictionary to keep track of the unique characters in each word. If there are multiple words with the same count, it returns the one that comes first in lexicographical order. It uses a set to determine the unique characters, and the dictionary stores the character count for each word, using `max` with a lambda function to compare the word with the highest character count and the lexicographical order as keys.