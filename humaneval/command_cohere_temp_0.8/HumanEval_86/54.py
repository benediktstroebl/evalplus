```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)

    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the provided example, the output for the input statements is:
```
Hi
ehllo
Hello !!!Wdlor
```