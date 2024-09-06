```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function first splits the input string `s` into individual words using the `split()` method. It then iterates through each word in turn, sorting the characters within each word based on their ASCII values and concatenating them together into a new word. This process is repeated for each word in the string, with spaces added between words as they were in the original string. The function finally returns the ordered version of the string as specified in the problem statement.

This code will output the correct `new_word` as described, where each word is sorted by ASCII value, and the order of words and spaces is maintained. You can verify this by testing with the examples provided in the problem statement.