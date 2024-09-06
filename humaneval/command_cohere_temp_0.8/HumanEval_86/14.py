```python
def anti_shuffle(s):
    word_arr = s.split()
    new_word_arr = []
    for word in word_arr:
        char_arr = list(word)
        char_arr.sort()
        new_word = ''.join(char_arr)
        new_word_arr.append(new_word)
    return ' '.join(new_word_arr)
```

This code defines a function `anti_shuffle` that takes a string as input and performs the specified task. It first splits the input string into individual words using space as the delimiter. Then, for each word, it creates a list of characters, sorts them alphabetically based on their ASCII values, and joins them back to form a new word. These new words are stored in the `new_word_arr` list. Finally, the function returns a space-separated string composed of the newly formed words, preserving the original word order and spaces.