```python
def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char == ' ']
    new_word_inds = [i for i, char in enumerate(s) if char != ' ']
    new_word = ''.join(char for i, char in sorted(zip(new_word_inds, s), key=lambda t: t[1]))
    new_word = new_word.replace(' ', '!!!')
    return ' '.join([s[i-1]:i in word_inds for i in range(len(s))]) + '!!!' * (len(s) - len(new_word)) + new_word
```

The function uses simple string manipulation and ascii sorting to achieve the desired result of reordering characters in each word, while keeping the order of words and spaces. You can test the function by calling it with different inputs to verify the correct behavior for each test case.