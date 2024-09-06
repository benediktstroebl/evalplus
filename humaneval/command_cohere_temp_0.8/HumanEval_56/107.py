```python
def correct_bracketing(brackets):
    open, closed = 0, 0
    for char in brackets:
        if char == '<':
            open += 1
        elif char == '>':
            closed += 1
        if open > closed:
            return False
    return open == closed
```

This Python script defines a function `correct_bracketing` that takes a string `brackets` as input. The function counts the number of opening and closing brackets within the string using two counters, `open` and `closed`, initialised to 0. It then iterates through each character in the input string, incrementing the `open` counter if it encounters an opening bracket (`<`) and the `closed` counter if it finds a closing bracket ('>'). Additionally, it checks whether the count of opening brackets is greater than the count of closing brackets during each iteration; if so, it immediately returns `False`, indicating that there are more opening brackets than closing brackets, and the sequence is not correctly bracketed.

After processing all characters, the function compares the counts of opening and closing brackets. If they are equal, it returns `True`, indicating that the brackets are correctly balanced with an equal count of openings and closings. 

The function returns `False` if the count of openings is not equal to the count of closings, implying that the brackets are not correctly balanced. This imbalance occurs when there are more opening brackets than closing brackets in the sequence.

The expected output for various test cases are:
```
True
False
True
False
```