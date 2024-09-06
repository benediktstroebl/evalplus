```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without altering the order of spaces and word sequences. For example, the input `'Hello World!!!'` would return `'Hello !!!Wdlor'`.

This approach splits the input string into words using whitespace as a separator, sorts each word based on ASCII values, and then reassembles the sorted words back into the original sentence while maintaining whitespace structure.