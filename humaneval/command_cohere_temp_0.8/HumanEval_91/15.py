```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers ('.' character) and iterates through every sentence. The `startswith()` function is used to check if the beginning of every sentence corresponds to the required pattern. The function returns the number of sentences that match the pattern. 

## Instructions Reminder:
This solution allows you to demonstrate your approach and provide an example of a potential solution. It is possible to utilize a different method, but your final solution should be equally efficient and concise. Let me know if you would like to elaborate on any specific aspect of the problem or the provided solution.