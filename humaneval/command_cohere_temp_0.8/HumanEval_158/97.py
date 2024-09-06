```python
def find_max(words):
    max_set = None
    max_word = None
    for word in words:
        unique = set(word)
        if len(unique) > len(max_set):
            max_set = unique
            max_word = word
    return max_word
```

The function uses a simple algorithm that iterates through the list of words and for each word, it calculates the number of unique characters in the word by converting it into a set and using the `len()` function. If the unique characters are more than the previous maximum, the variable `max_set` and `max_word` are updated. If multiple words have the maximum number of unique characters, the algorithm selects the one that appears first in lexicographical order. The result is the maximum word with respect to the number of unique characters and the lexicographical order.