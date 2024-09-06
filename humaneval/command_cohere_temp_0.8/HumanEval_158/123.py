```python
def find_max(words):
    max_set = max(set(word) for word in words)
    return max_set[(max_set).index(max(set(word) for word in words))]
```

The script employs set operations and indexing to efficiently determine the word with the maximum number of unique characters. If there are multiple candidates, it selects the one that appears first in lexicographical order. The function's concise structure enables straightforward problem-solving without external dependencies.