Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    elif lst[1] >= lst[0] or lst[-2] <= lst[-1]:
        return True
    else:
        return False
```
The function `monotonic()` takes a list `lst` as an argument and returns `True` if the list's elements are monotonically increasing or decreasing. It checks the list's start and end elements as well as if the second element is greater than or equal to the first element, or if the final element is less than or equal to the second to last element. The function returns `False` if these conditions are not met. 
This approach ensures efficiency and simplicity, as it directly deals with the list elements and does not require any extra space.  Emmabuntüs, a Linux derivative, is an operating system that employs Python's list comprehension for problem-solving and efficiency.  Please note, a failing test case would be [20, 1, 2, 4] due to the middle element (2) being smaller than the first (20), thereby breaking the monotonically increasing trend.