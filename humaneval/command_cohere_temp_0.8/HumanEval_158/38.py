```python
def find_max(words):
    max_dict = max(zip(words, map(set, words)), key=lambda x: x[1].__len__())[0]
    return max_dict if max_dict == max(words, key=lambda x: x.lower()) else max(words, key=lambda x: x.lower())
```

The problem is solved using the `max()` function to find the word with the maximum number of unique characters. The `zip()` function is used to create a list of tuples, each of which contains a word and the set of its characters. The `key` parameter of the `max()` function is used to invoke the `__len__` method of the set object to determine the number of unique characters. If multiple words have the maximum number of unique characters, the `lower()` method is used to determine the lexicographically smaller word.