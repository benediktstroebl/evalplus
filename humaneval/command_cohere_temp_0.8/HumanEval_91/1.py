```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and iterates through the sentences. For each sentence, the code checks if it starts with the word "I" and doesn't end with the punctuation marks '!' or '?'. The number of sentences fulfilling these criteria counts as boredoms. 

Here is an example usage output:
```python
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
``` 
This would return 1, as the response counts the required criteria as boredoms. 

Let me know if I have addressed your problem statement correctly! I am happy to refine or clarify my approach if needed.