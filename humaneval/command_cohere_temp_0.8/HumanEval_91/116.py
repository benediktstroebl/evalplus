```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('. ') :
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('.') > -1:
            cnt += 1
    return cnt
```

This approach uses split and join operations on the space character to break down the input string into sentences and then checks if the sentence starts with 'I' and has a period mark in it, which indicates a sentence end. Consequently, the function counts the number of sentences that match the criteria and returns the count.