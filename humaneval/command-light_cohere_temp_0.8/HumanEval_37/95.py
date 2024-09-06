```python
def sort_even(lst):
    even = [el for el in lst if el % 2 == 0]
    return even + [el for el in lst if el % 2 != 0]

# Test cases
test_sort_even = [
    ( [1, 2, 3], [1, 2, 3]),
    ( [5, 6, 3, 4], [3, 6, 5, 4])
]

# Function call and check results
for t in test_sort_even:
    actual = sort_even(t)
    expected = [3, 6, 5, 4]
    assert actual == expected, f"Failed for {t}!"
```