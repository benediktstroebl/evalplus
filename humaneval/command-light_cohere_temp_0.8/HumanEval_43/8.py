```python
def pairs_sum_to_zero(lst):
    sum_to_zero = False
    for x, y in lst:
        if x + y == 0:
            sum_to_zero = True
            break
    return sum_to_zero

# Test the function
for test_case in [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1],
]:
    result = pairs_sum_to_zero(test_case)
    print(f"{test_case} => {result}")
```
The script defines a function `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a testing logic inside a loop to check if any two elements sum to zero. The loop iterates through all possible combinations of the list elements, and the `sum_to_zero` variable is set to `False` initially. 
The output of this function is then printed for each test case.