```python
def find_max(words):
    char_count = {}
    lexic_front = {}
    for word in words:
        unique_chars = len(set(word))
        if unique_chars not in char_count:
            char_count[unique_Chars] = 1
        else:
            char_count[unique_chars] += 1
        lexic_front[unique_chars] = word

    max_count = max(char_count.values())
    return min(lexic_front, key=lambda x: char_count[x] != max_count)
```

The function uses dictionaries to count the unique characters and to store the front lexicographical word for each unique character count. The max character count is found in the `max` function. The script returns the word that has the max unique character count and is the front lexicographically using the `min` function.