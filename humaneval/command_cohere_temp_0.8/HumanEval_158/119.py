```python
def find_max(words):
    char_count = {}
    max_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        num_unique = len(unique_chars)
        if num_unique > max_count:
            max_count = num_unique
            result = word
        if num_unique == max_count:
            if word < result:
                result = word
    return result
```

The code defines a function `find_max` that takes in a list of strings, specifically words. It examines each word, tracking the number of unique characters encountered among all the words. The code maintains a count of the most frequent number of unique characters and the word associated with this count. It then returns the word that not only has the highest count of unique characters but is also the lexicographically earliest among those with the same count.

The approach leverages the innate properties of sets in Python, where each unique character only appears once within the set, thereby making membership tests and count operations efficient and straightforward.