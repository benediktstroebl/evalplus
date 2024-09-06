```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            close += 1
        if open > close :
            return False
        open -= 1
        close -= 1
    return True
```

The function counts the open and closed brackets accordingly, and if the closing brackets don't catch up with the opening ones, the whole sequence is invalid. Meanwhile, if the total count of opening brackets ever exceeds the closing ones, it still qualifies as a valid nested sequence since the latter part of the sequence can make up for it. Thus, the function returns true if there is at least one valid subsequence with nested brackets.

The given examples illustrate how the function uses the mentioned algorithm to validate the input strings accordingly.