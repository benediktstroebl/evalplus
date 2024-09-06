```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` splits the input string into a list of words and then constructs a new word where each character is sorted in ascending order based on its ASCII value. It does this for each word in the input string, maintaining the order of words and spaces. The resulting 'ordered version' of the string is returned.