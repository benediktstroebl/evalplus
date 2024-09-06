```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(digits) // 2)
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

The solution leverages Python's innate subtraction capabilities to readily count the odd digits within a string of digits. The function accepts a list of such strings, and subsequently produces a new list of messages, wherein each message indicates the count of odd digits within the corresponding string from the input list.

This solution adheres to the problem statement's directive to use only the digits of each string for the odd count. Hence, it avoids the potential mistake of also considering the length of the string itself as a digit.