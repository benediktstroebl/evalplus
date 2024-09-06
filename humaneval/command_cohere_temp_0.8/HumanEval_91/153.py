```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach breaks the input string into separate sentences by splitting it at each period (`.`) and then checks if each sentence starts with the word `I`. The `strip()` method removes any leading or trailing whitespace, including periods, to ensure accurate counting of boredoms. 

To test this script, you can call the `is_bored()` function with different input strings and verify the output against the expected count of boredoms. 

Let me know if you need any further adjustments or if you want to tackle another coding problem!