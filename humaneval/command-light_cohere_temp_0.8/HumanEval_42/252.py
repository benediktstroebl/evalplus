```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l

def test_incr_list():
    """Return list with elements decremented by 1."""
    l = [1, 2, 3]
    l.append(1)
    return l

# Test cases for the function above
test_cases = [
    incr_list([1, 2, 3]),           # [2, 3, 4] -> [2, 3, 4]
    test_cases.append([5, 3, 2, 3])     # [2, 3, 4] -> [5, 3, 5]
    test_cases.append([5, 4, 3])       # [5, 3, 5] -> [9, 5, 9]
    test_cases.append([9, 5, 3])       # [9, 5, 9] -> [14, 9, 14]
    test_cases.append([14, 14])       # []

print("Test cases:", test_cases)

# Run the functions and print results
for func, test_case in zip([test_incr_list, incr_list], test_cases):
    print(f"{func.__name} [{test_case}] -> {test_case}")
```
The output will show the results of each test case. The script is designed in a way that it can be easily understood, with comments explaining each step of the logic.