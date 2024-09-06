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

The function counts the openings and closings of square brackets using two counters. When going through the string, whenever a square bracket is encountered, the corresponding counter is incremented. If at any point the number of openings is greater than the closings, it returns `False` since a closing bracket was not found for every opening bracket. If at the end the two counters are not equal, it returns `True` as there is at least one nested bracket. 

The markdown code block provided in the question describes different test cases and the expected output for the `is_nested` function. If the output of the function corresponds to the expected output, the code block will output ````Python
PASS
````. Otherwise, it will output ````Python
FAIL
````.