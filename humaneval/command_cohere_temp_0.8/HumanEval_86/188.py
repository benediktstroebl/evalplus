```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)

    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (using the split() method, which knows to split on spaces) then sorts each word based on ASCII value and finally joins the ordered words back together into your new string.

The sorted() method in Python sorts string letters based on their ASCII value, guaranteeing that 'a' < 'z' < 'A' < 'Z'.