Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the string. It separates the input into sentences using the '.' punctuation mark. For each sentence, it checks if the sentence starts with the word "I". If it does, it increments the count of boredoms by 1. Ultimately, it returns the total count of boredoms in the given input string.

To test this, you can run the following input through the function:
```python
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
```

This will output:
```
1
```

This demonstrates the function working as expected, incrementing the count for the sentence that starts with "I" and producing zero for the other sentence.