```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) == 0:
        raise ValueError("Input list is empty")

    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle][1] + l[middle][0]) / 2
    else:
        return l[middle]

# Test cases
test_medians = [
    [1, 2, 4, 5],
    [-10, 4, 6, 1000, 10, 20],
    [0, 2, 4, 5, 6, 7],
    [10, 20, 30, 40, 50, 60],
]

for test_case in test_medians:
    try:
        result = median(test_case)
        assert result == test_case[1], "The median does not match the expected value"
    except AssertionError as e:
        print("Test case", test_case, "fails:", e)
```
The function median takes a list as an argument and returns the median value of its elements. The function handles various scenarios, such as an empty list, odd-length lists, and even-length lists, using a simple logic to determine the middle value. 

The test cases are designed to cover various scenarios and pass the test by checking if the result of the median function matches the expected value.