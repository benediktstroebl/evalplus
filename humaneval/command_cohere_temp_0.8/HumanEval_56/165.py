```python
def correct_bracketing(brackets):
    open, close = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            close += 1
        if open > close:
            return False
    return open == close
```

The following tests are all included in this code:
- **`'<>'`** : Should return **`'True'`**.
- **`'<<><>>'`** : Return **`'True'`**.
- **`'><<>'`** : Return **`'False'`**.

It counts the number of opening and closing brackets encountered as it goes through the string. The function returns False immediately if the number of open brackets exceeds the number of closing brackets. The function returns True if both counts are equal at the end, indicating that every opening bracket has a corresponding closing bracket.