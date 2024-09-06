```python
def median(l: list):
    """Return median of elements in the list l"""
    assert len(l) > 1, "List must have at least two elements"
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test cases
for test in [median([3, 1, 2, 4, 5]), median([-10, 4, 6, 1000, 10, 20])]:
    assert test == 15.0, "Incorrect median not calculated"
```
The provided Python code defines a function called `median` that calculates the median of a list's elements. The function uses an algorithm to determine the median when the list has an even number of elements and when it has an odd number of elements, it returns the middle element. 

The code then provides a series of test cases to verify the correctness of the `median` function. The test cases cover various scenarios, such as lists with even or odd lengths and elements, and the function's output is compared against the expected result (`15.0`) to pass the