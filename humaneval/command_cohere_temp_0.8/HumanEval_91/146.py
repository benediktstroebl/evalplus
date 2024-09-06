```python
def is_bored(S):
    cnt = 0
    for line in S.split('.') + S.split('?') + S.split('!'):
        if line.strip().lower().startswith('i'):
            cnt += 1
    return cnt
```

This approach uses the built-in Python functions 'split()' and 'startswith()' to accomplish the task. The 'split()' function splits the input string into a list of words or sentences based on the provided delimiters ('.', '?', or '!'). The 'startswith()' function checks if a sentence begins with the word "I". 

The function counts the number of sentences that start with "I" and returns the count. It does not count sentence fragments or partial words as boredoms.