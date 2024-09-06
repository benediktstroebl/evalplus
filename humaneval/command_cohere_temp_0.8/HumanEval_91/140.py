```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This Python script defines a function called `is_bored` that takes a string as an input parameter and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". The function splits the input string into a list of sentences using the sentence separator '.' and then iterates through each sentence to check if it starts with 'I'. If a sentence starts with 'I', it increments the counter by 1. The function returns the total count of boredoms in the input string.