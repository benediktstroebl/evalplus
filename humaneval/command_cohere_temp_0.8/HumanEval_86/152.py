```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        new_word = ''.join(sorted(word))
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (or arrays of characters separated by spaces). Then, for each word, it sorts the characters alphabetically, and then joins them to produce a new word. Finally, these new words are joined back by spaces to form the answer. 

Would you like to know more about any of the steps involved in this solution? Don't hesitate to ask!