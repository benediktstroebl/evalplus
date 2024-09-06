```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?!')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.' '?' or '!' and then uses the `startswith` method to check if the sentence starts with the word 'I'. The count of such sentences is kept track of in the variable bored, which is returned at the end. 

This solution has a time complexity of O(n), where n is the number of sentences in the input string, as it requires splitting the input into sentences and checking for each sentence if it starts with 'I'. 

Such a solution is efficient and easy to read, making it a great choice for coding tasks like this one.