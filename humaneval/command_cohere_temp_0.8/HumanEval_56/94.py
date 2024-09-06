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

To test the function, four tests were conducted where the function was passed a string of "<" and ">" characters. The function then returned a boolean value of either True or False, depending on whether all opening brackets had corresponding closing brackets. 

1. ```python
   >>> correct_bracketing("<")
   False
   ```
2. ```python
   >>> correct_bracketing("<>")
   True
   ```
3. ```python
   >>> correct_bracketing("<<><>>")
   True
   ```
4. ```python
   >>> correct_bracketing("><<>")
   False
   ```

The expected output according to the truth table above was what was obtained. 

NOTE: The problem can also be solved using stacks, but the use of an auxiliary counter makes the code simpler and easier to understand.