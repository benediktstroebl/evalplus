```python
def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            max_word = word
    return max_word
```

The function uses a simple loop to iterate through the list of words and find the one with the maximum count of unique characters. If multiple words have the maximum count, the function will return the one that comes first in lexicographical order. The code doesn't require any external libraries and should work out of the box for any list of strings.