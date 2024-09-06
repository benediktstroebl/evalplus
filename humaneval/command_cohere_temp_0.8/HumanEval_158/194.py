```python
def find_max(words):
    char_count = {}
    lexicographical_order = []
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        lexicographical_order.append((char_count[word], word))
    return min(lexicographical_order)[1]
```

The code defines a function `find_max` that takes in a list of strings, `words`. The function aims to find the word with the maximum number of unique characters among these words while also considering words with the same maximum uniqueness level in lexicographical order. 

Here is an example usage of the function:
```python
print(find_max(["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]))
```
The output will be:
```
aaaaaaa
```

This means that the function will return the word "aaaaaaa" because it has the maximum number of unique characters among the given list of words, and it is also the first in lexicographical order among the words with the same maximum number of unique characters.