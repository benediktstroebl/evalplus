```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers ('.' punctuation mark) and iterates through every sentence. The function checks if the sentence starts with the word "I" and does not end with an exclamation mark or a question mark. If those conditions are fulfilled, the count is incremented by one. Ultimately, the function returns the number of sentences that match the given criteria. 

 hashtree_test_is_bored_1.txt  hashtree_test_is_bored_2.txt