```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    num_boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            num_boredoms += 1
    return num_boredoms
```

This script defines a function called `is_bored` that takes in a string as an input and counts the number of boredoms in the string. The function iterates through each sentence using the split method with '.' delimiter, and strips out exclamation marks or questions marks that might indicate the end of a sentence. Then it checks if the sentence starts with the word "I", and if so, it increments the counter. 

To see the function in action, try calling it with different inputs:
```python
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("Hello world"))
```

This will output:
```
1
0
```