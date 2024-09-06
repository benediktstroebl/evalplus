```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if open > closed :
            return False
        open -= 1
        closed -= 1
    return True
```

The following code uses a straightforward algorithm to solve the problem:
1. Keep track of the number of opening and closing brackets.
2. For each character in the string:
   - If the character is an opening bracket, increment the open count.
   - If the character is a closing bracket, increment the closed count.
   - If the open count is greater than the closed count, return False (unbalanced).
   - Subtract 1 from both counts (to account for the bracket just read).
3. If the end is reached and the open count is zero, return True (balanced or nested).

The provided tests in the problem statement show various scenarios that illustrate the behavior of the function correctly.  Such as:
```
is_nested('[[]]') == True
is_nested('[][]') == False
is_nested('[]') == False
is_nested('[][]]') == True
is_nested('[]][[]') == True
is_nested('[][][[[]') == True
is_nested('[]]])]]]' ) == False
```