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
    return True
```
The algorithm is a simple bracket checker. The `open` and `closed` variables keep track of how many square brackets of each type we have encountered. When a closing bracket `]` is encountered, we check if we have a matching opening bracket [ to correspond to it. If at any point the count of closed brackets exceeds the count of open brackets, it means there is a mismatch and the function returns False. If we finish going through the string and the count of open brackets is equal to the count of closed brackets, it means all brackets were matched correctly and at least one bracket was nested, so the function returns True.

The provided solution achieves a O(n) time complexity, where n is the size of the string. It does so by checking the brackets with equality checks, which makes it run in constant time for each bracket. Since we have to check all brackets, the overall time complexity is O(n).