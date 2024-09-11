```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or \
           all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
if monotonic([1, 2, 4, 20]):
    print("Test case 1: True")
if not monotonic([1, 20, 4, 10]):
    print("Test case 2: True")
if monotonic([4, 1, 0, -10]):
    print("Test case 3: True")
```

In this script, we define a function `monotonic` that takes a list `l` as input. It uses the `all` function with a generator expression to check if all adjacent elements in the list are either less than or equal to (for increasing) or greater than or equal to (for decreasing) each other. If either condition is met, it returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior.