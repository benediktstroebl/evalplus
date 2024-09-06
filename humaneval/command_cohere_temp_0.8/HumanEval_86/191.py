```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. For example, the following call:
```python
print(anti_shuffle("Hello World!!!"))
```
Will print:
```
Hello !!!Wdlor
```

The above example is meant to illustrate how the function sorts strings based on ASCII values while retaining word order.