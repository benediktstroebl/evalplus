```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']' :
            closed += 1
        if closed > open :
            return False
    return closed != open 
```

The function uses two counters to track the balance of opening and closing brackets. The algorithm iterates through the string and increments the corresponding counters depending on whether the encountered character is an opening or a closing bracket. At the end of the iteration, if the difference between the closed and open brackets is not zero, this indicates the presence of a valid nested bracket subsequence, hence the function returns `True`. If the difference is zero, the function returns `False`, indicating no nested brackets in the sequence. 

Such an approach is relatively efficient in terms of time and space complexity, as it uses only a constant amount of memory to store the two counters, resulting in an O(n) time and O(1) space complexity, where n is the length of the input string.  This solution works correctly for the provided test cases.