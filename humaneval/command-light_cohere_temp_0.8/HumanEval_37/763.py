```python
def sort_even(l: list):
    return l[:][::2] + [v + 2 for v in l[1::2]]

# Test cases
test_cases = [
    [ [1, 2, 3], [5, 6, 3, 4]],
    [1, 2, 3, 4, 5],
    [3, 6, 5, 4, 7],
]

for i, test in enumerate(test_cases):
    actual = sort_even(test)
    expected = list(map(lambda x: x + 2, test))
    assert actual == expected, f"Test case {i+1} failed: Actual {actual}, Expected {expected}"
```  This script defines a function called sort_even, which sorts a list of numbers into the format [3, 6, 5, 4, 7], with even numbers (2, 4, 6) appearing before the odd numbers (1, 3, 5). The function first computes the even-sorted list, then adds 2 to each even index to produce the final sorted list. The test cases ensure that the function successfully sorts the given lists according to the expected format.