```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [i+1 for i in l] + l
    return res

#Test case 1: Basic function call
assertEqual([1, 2, 3], incr_list([1, 2, 3]))

#Test case 2: Existing list
assertEqual([5, 3, 5, 2, 3, 3], incr_list([5, 3, 5, 2, 3, 3]))

#Test case 3: Duplicate element
assertEqual([5, 3, 5, 2, 3, 3], incr_list([5, 3, 5, 2, 3, 3, 5]))

#Test case 4: Empty list
assertEqual([], incr_list([]) )

#Test case 5: Single element
assertEqual([6], incr_list([6]))
```
The function incr_list creates a new list with elements from the input list incremented by 1, then it adds the original list to that new list. The test cases cover a wide range of scenarios to test the correctness of the function.