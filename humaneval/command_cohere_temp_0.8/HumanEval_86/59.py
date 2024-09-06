```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (using `split()` method on the string), sorts each word based on ASCII values, and then joins them back to produce the required 'ordered' version of the string. Lastly, the function returns the ordered string. The output of the given examples will be:
```bash
'Hi'
ehllo
Hello !!!Wdlor
```