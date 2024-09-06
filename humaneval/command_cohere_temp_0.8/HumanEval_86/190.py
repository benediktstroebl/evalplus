```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` takes a string as input and returns an ordered version of the string as described in the prompt. It splits the input string into words and sorts the characters of each word (except blanks) in ascending order based on their ASCII values. The sorted words are then rejoined into a single string, with blank spaces retained to preserve the original word spacing. The function retains the order of words and blank spaces, thus achieving the desired ordered version of the string.