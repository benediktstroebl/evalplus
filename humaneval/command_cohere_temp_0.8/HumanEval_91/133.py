Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            count += 1
    return count
```

This function counts the number of boredoms in the given string `S`. It splits the string using the punctuation marks '.' as separators and iterates through the resulting sentences. For each sentence, it uses `strip()` to remove leading and trailing whitespaces and checks if the sentence starts with the word 'I'. If it does, it increments the count. Finally, it returns the total count of boredoms found in the input string.