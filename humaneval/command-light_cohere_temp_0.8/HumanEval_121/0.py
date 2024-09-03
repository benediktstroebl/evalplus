```python
def solution(lst):
    """Given a non-empty list of integers, returns the sum of all odd elements in even positions."""
    return sum(x for x in lst if x%2 != 0 and (x < 0) == (lst[0] < 0))
```
This function takes a list of integers as input and iterates through the list. The function checks for odd elements in even positions, and the first element in the list. It returns the sum of these odd elements.