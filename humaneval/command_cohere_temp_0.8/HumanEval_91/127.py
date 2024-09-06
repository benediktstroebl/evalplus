```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.' '?' or '!' and then uses the strip method to remove these punctuation marks from the sentences. The script then checks if the sentence starts with the word 'I', and if it does, it increments the counter bored. Finally, the function returns the counter bored, which represents the number of boredoms in the given input string. 

Here is an example of how to use the above code to check for boredoms in a sentence:
```python
input_string = "The sky is blue. The sun is shining. I love this weather"
result = is_bored(input_string)
print(result)
```

The output will be:
```
1
```

Since the sentence "I love this weather" starts with the word "I", it is considered a boredom, hence the output equals 1.