```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` splits the input string into a list of words and then sorts the characters in each word (preserving spaces between words) based on their ASCII values, producing the desired "ordered version" of the input string.