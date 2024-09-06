```python
def max_element(lst):
    if not_greater_than(lst) or not lst:
        return float('-inf')
    return max(lst)

def not_greater_than(lst):
    return any(x > float(lst[0]) for x in lst)

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element([1, 2, 3, -1000, 4, -5, 5, 6])))
    print(max_element([[-1, 2], [3, 4], [5, 6]]))
```

This code provides a function `max_element` that calculates the maximum element in a given list. The function also has a helper function `not_greater_than` to check if any element in the list is greater than a specific value.  The test of the function with a variety of test cases.