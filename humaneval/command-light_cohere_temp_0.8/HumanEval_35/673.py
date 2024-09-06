```python
def max_element(lst):
    if not_max == lst[0]:
        not_max = lst[1]
    else:
        not_max = lst[0]
    for num in lst[1:]:
        if num > not_max:
            not_max = num
    return not_max

# Test cases
tests = [
    "Input: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    "max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123"
    "Input: [-2, 0, 4, -6]
    "max_element([-2, 0, 4, -6]) == -6"
    # ... other tests ...

for _ in range(2):  # Test case iteration
    status = unittest.run(max_element, tests[__enter__()])
    print(f"Test {_}:\t{status}")
```
The function max_element takes a list lst as input and returns the maximum element in the list. It compares the max element to the first element in the list and updates the variable not_max with the larger value.  It then loops through the for each element in the list and updates not_max if the current element is greater than not_max.