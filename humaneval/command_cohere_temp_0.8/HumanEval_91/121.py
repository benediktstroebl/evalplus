```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            count += 1
    return count
```

This approach splits the input string by the sentence delimiters '.' and iterates through the resulting sentences. For each sentence, it removes question mark ('?') and exclamation mark ('!') if they are present at the end of the sentence (using the strip() method). Then it checks if the sentence starts with the word 'I'. If so, it increments the counter `count`. Finally, the function returns the total count of boredoms.

Note that this approach assumes that the input string contains only English sentences and that 'I' is always capitalized. If the input might contain other languages or variations in case, further processing would be necessary.