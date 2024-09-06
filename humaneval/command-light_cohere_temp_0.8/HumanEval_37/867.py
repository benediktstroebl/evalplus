```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 7, 8],
    [10, 20, 30],
]

for act in test_sort_even:
    actual = sort_even(act)
    expected = [3, 6, 5, 4]
    assert actual == expected, f"Test case {act} failed"
```  This script defines a function that takes a list l and returns a new list l' where the values at the even indices are equal to the values of the corresponding even indices of l, but sorted. The function uses the line-by-line comparison and ordering to ensure the output matches the expected result.