```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach breaks the input string into separate sentences by splitting at each period, and then strips any extra whitespace from each sentence. It then checks if the sentence starts with the word 'I', and if so, increments the counter. Finally, it returns the total count of sentences that start with 'I'. 

This should accurately solve the described problem, given that the input string contains entire sentences separated by periods, with potentially some whitespace and punctuation. Let me know if you'd like me to explain any part of the solution or provide further insights!