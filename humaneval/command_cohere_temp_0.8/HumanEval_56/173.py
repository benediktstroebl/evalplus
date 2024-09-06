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

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the opening and closing brackets within the string using two counters, `open` and `close`, initialised to 0. It then iterates through each character in the input string, incrementing the `open` counter if the character is an opening bracket '<' or the `close` counter if the character is a closing bracket '>'. Additionally, it checks if the number of opening brackets is greater than the number of closing brackets during iteration; if so, it returns False, indicating that there are more opening brackets than closing brackets. After processing all characters, the function returns True only if the counts of opening and closing brackets are equal, signifying that the brackets are correctly balanced.