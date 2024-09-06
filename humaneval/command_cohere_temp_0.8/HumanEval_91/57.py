```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". The function splits the input string into a list of sentences using the sentence markers '.' and counts the number of boredoms in the list. Finally, it returns the count of boredoms.

The expected output for the given examples is:
```
0
1
```

This script provides a clear and concise solution to the problem using Python. It maintains the code's readability and efficiency, making it suitable for solving the problem statement while adhering to Python best practices.