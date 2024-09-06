```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, we iterate over the words, ordering the characters using the `sorted()` function and joining them together to form a new word. This new word is then added to the `new_word_array`. Finally, we join the array of new words together with spaces to form the final ordered string.

The expected output for the test cases provided in the prompt is:
```
'Hi'
'ehllo'
'Hello !!!Wdlor'
``` 

This solution maintains the order of words and spaces, and reorders the characters within each word based on the ASCII values.