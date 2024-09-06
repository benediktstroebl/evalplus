```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function works by comparing the unique characters in both strings and checking whether more than 60% of the characters are the same. 

To test this, could you provide some test cases that demonstrate the function's behavior? Include a few tests that should pass and some that should fail. Add them in markdown code blocks with the ```pytest ``` syntax, and I'll help validate the solution.