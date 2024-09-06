```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using the `split()` method (preserving the blank spaces), then sorts each word based on the ASCII value of its characters, and finally, rejoins them to form the ordered version of the input string.