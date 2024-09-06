Here's a Python script with a self-contained function that solves the problem:
```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

This script splits the input string into words and then joins each word separately, sorting the characters in ascending order. It then rejoins the sorted words with spaces in between to form the ordered version of the input string, as per the problem description.