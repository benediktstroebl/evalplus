```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and '!?'. The resulting sentences are then checked for the presence of the prefix 'I', and the count of sentences starting with 'I' is returned. The `strip()` method is used to remove '!?' from the ends of sentences. This ensures that the punctuation doesn't count as part of the sentence for the purposes of the check. 

Such sentences could be considered boring as they revolve predominantly around the 1st person pronoun, indicating a lack of verbality and engagement.