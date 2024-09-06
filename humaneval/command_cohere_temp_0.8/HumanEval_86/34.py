```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` splits the input string into a list of words and then sorts the characters in each word (except blanks) in ascending order based on their ASCII values. It then joins these sorted words back together with spaces in between to form the ordered version of the input string, as described in the prompt.