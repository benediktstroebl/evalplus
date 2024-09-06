```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        new_word = ''.join(sorted(word))
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using `split()` and then for each word, it sorts the characters alphabetically and joins them back to form a new word. Finally, the new words are joined with spaces to form the `ordered version of the string`.