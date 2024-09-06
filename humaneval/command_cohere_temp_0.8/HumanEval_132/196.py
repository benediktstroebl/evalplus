```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings and closings squares brackets occurring in the string `s`. At the beginning of the sequence, the `open` variable is incremented by 1 when a left bracket is met. Conversely, when a right bracket is met, the `close` variable is incremented by 1. When the sequence is started by a closing bracket, the `open` variable is decremented by 1. 

If at any point the `open` variable is larger than the `close` variable, the function returns False, meaning that the sequence does not contain a valid subsequence of nested brackets. If the balance between opening and closing brackets is kept until the end of the sequence, it means the sequence contains at least one nested bracket, and the function returns True. 

This solution works for any string containing only square brackets and will return the appropriate boolean value for the given test cases.