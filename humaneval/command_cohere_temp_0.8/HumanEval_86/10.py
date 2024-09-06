```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, it iterates through each word, sorting the characters based on their ASCII values and joining them back together into a new word. The function assembles the new words back into a string with the original spacing and returns the ordered version of the input string.