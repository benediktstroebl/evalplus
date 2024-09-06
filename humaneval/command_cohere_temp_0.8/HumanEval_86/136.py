```python
def anti_shuffle(s):
    word_arr = []
    word_start = False
    blank_start = True
    for c in s:
        if not blank_start and not word_start and c.isalpha():
            word_start = True
            word_arr.append(c)
        elif not blank_start and word_start and c.isspace():
            word_start = False
            word = ''.join(word_arr)
            s = s.replace(word, ''.join(sorted(word)))
            blank_start = False
            word_arr = []
        else:
            blank_start = False
            word_arr.append(c)
    return s
```

The algorithm processes the string and creates an ordered version of it, where each word is sorted by its ASCII value. Here are the steps of the algorithm:
1. Initialize an empty `list` called `word_arr`, which will store the characters of each word encountered.
2. To determine whether the current character is the start of a new word or not, a `word_start` variable is used.
3. A `blank_start` variable is also initialized as `True` at the start of the loop. It denotes whether the current character is the first character of the string or not.
4. For each character in the string, the following conditions are checked:
   - If it's the start of a word (not the first character of a blank space), and it's an alphabetic character, we turn on the `word_start` flag and append the character to the `word_arr` list.
   - If it's after a word has started, and it's a blank space, then the `word_start` flag is turned off, and we concatenate the accumulated word into a single string. We then replace this concatenated string with its sorted counterpart in the original string `s`. After this step, both `blank_start` and `word_start` are reset to False, and `word_arr` is emptied for the next word.
   - If none of the above, it must be a punctuation mark or other non-alphabetic/non-blank character, so we simply reset `blank_start` to False. We still append the character to `word_arr` since it might be the first character of a new word.

This algorithm effectively creates an ordered version of the string, ensuring that words are sorted based on ASCII values while maintaining the original word order and spacing.