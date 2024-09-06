```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the provided example, the output for `anti_shuffle('Hello World!!!')` would be `'Hello !!!Wdlor'`, which is correct. 

This approach splits the input string into words using whitespace as the delimiter. Then, it sorts the characters in each word based on their ASCII values and joins them back together to form the final sorted string.