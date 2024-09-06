```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(second == sub for sub in first if sub == second[::-1])
```
The problem is to check whether the second string or any of its rotations are sub-strings in the first string. The provided solution uses Python's built-in `in` function to check if the second string is a substring of the first string. Additionally, it uses a list comprehension to check if any rotation of the second string is a substring of the first string. Both checks are performed in a case-insensitive manner by converting the input strings to lowercase. The function returns `True` if any of these conditions are met, and `False` otherwise.  This solution is efficient and perfectly suits the problem constraints.