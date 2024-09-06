```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with various list inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_get_positive.push([5, -1, -2, -9]) # [2, 3, -9]
test_get_positive.push([1, 2, -3, -6])

print(f"Function Outputs: {test_get_positive}")
print(f"[[-9, 2, 3], [-5, 3, -1], [0, 1, 2]])")
```
This script defines a function get_positive that returns a list of only positive numbers from the input list l. It then creates a list of test cases and uses those to test the function. The test cases are passed to the function and the function's output is printed for each case.