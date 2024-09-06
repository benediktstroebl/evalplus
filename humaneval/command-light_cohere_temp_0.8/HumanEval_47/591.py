```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list cannot be empty.")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
tests = {
    "Test 1": median([3, 1, 2, 4, 5]),
    "Test 2": median([-10, 4, 6, 1000, 10, 20]),
    "Test 3": median([10, -10, 20, -30, 40, -20])
}

for name, test in tests.py.show(f key (`name`, test))
``` 
This script defines a function median that calculates the median of a list. The test cases are passed to test the function to verify its correctness.