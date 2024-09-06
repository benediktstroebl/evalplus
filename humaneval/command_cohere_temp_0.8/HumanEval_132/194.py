```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        else:
            closed += 1
        if closed > open:
            return False
    return open != 0
```

The function counts the opening and closing brackets iterating through the string. When a closing bracket appears, it checks if there is a matching opening bracket. If at any point the number of closings is greater than the number of openings, the bracket sequence cannot be nested, and the function returns `False`. If the number of openings is not zero at the end (i.e., there is an unclosed bracket), it also returns `False`. Otherwise, it returns `True`, indicating a valid nested sequence. 

This solution is efficient since the total time complexity is O(n), where n is the length of the input string, and the space complexity is O(1) since it only monitors the opening and closing brackets on the stack without any additional data structures.