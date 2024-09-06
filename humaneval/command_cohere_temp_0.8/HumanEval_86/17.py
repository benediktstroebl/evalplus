```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without altering the word order in the string. In the provided example, the output for each test case is correctly computed and returned. The code is concise and effective in solving the problem using a split-and-sort approach.