```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is a sentence that starts with the word "I". The function splits the input string into a list of sentences using the sentence delimiter '.' and then iterates through each sentence, trimming any leading or trailing white spaces using the `strip()` method. If a sentence starts with the word "I", it increments the counter `bored` by 1. Finally, the function returns the count of boredoms in the input string.