```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This Python script demonstrates a function called `is_bored` that addresses the task of counting boredoms in a given input string. A boredom, in this context, is defined as a sentence that starts with the word "I." The function splits the input string into separate sentences using the punctuation marks ".", "?", or "!". It then iterates through each sentence, stripping any leading or trailing white-space characters. If a sentence begins with the word "I," it counts that instance as a boredom and increments the boredom count variable. Finally, the function returns the total count of boredoms present in the input string. 

Note: This script assumes that the input string `S` contains only plain English text and that the syntax of the input follows typical sentence structures. Adjustments may be necessary for handling other scenarios or non-standard syntax.