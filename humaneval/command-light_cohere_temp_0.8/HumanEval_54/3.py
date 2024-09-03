```python
def same_chars(s0: str, s1: str):
    return len(set(s0)) == len(set(s1))

# Example function test cases
same_chars('eabcd', 'dddddddabce')  # False
same_chars('eabcd', 'uddffdd')         # False
same_chars('aaaaaa', '123')           # True
same_chars('abcdef', 'ickness')     # True
same_chars(' coworker , developer', 'developer , coworker') # True
```
The function checks if the lengths of the set of characters in two strings are equal. It returns True if they character sets have the same length.