```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            count += 1
    return count
```

This approach splits the input string by the sentence delimiters '.' and iterates through each sentence. For each sentence, the leading punctuation marks '!' and '?' are stripped and the phrase starting with "I" is counted. The total count of boredoms returns as a result. 

This solution should accurately address the boredom-counting challenge as outlined in the problem statement. Feel free to test it out with different input variations. If you'd like to delve further into the topic or explore more complex scenarios, don't hesitate to ask.