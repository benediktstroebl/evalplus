Here's a Python script that solves the anti-shuffle problem:
```python
def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not blank_start and not word_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif blank_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif not c.isalpha():
            if word_start:
                word_arr.sort()
                word_start = False
            blank_start = False
        else:
            blank_start = True
    if word_start:
        word_arr.sort()
    return ' '.join(word_arr)
```

This script takes a string and creates an ordered version of it, where all the words are replaced by a new word where all the characters are arranged in ascending order based on their ASCII value. The script makes sure to keep the order of words and blank spaces in the original string.

The code uses a loop to traverse the input string character by character. It maintains two boolean variables, `word_start` and `blank_start`, to keep track of whether the current character is starting a new word or a blank space. When the script detects the start of a new word (i.e., an alpha character after a blank space or at the beginning of the string), it appends the characters to the `word_arr` list. Later, if a new word is detected but `word_start` is still true, the characters are sorted in ascending order based on ASCII value, simulating the desired shuffling behaviour. The script ensures that non-alphabetic characters and blank spaces do not affect the sorting process. Finally, the ordered word segments are joined together with spaces using `join` to form the output string, and the `word_start` boolean is reset for accurate tracking in subsequent iterations.