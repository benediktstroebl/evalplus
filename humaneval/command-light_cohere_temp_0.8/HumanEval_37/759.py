```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 != 0]

# Test the function with various inputs

test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [10, 20, 30],
    [3, 6, 5, 4]
]

for test in test_cases:
    even = sort_even(test)
    assert len(even) == 3, f"Test case {test} failed: length expected 3, got {len(even)}"
    assert even == [3, 6, 5], f"Test case {test} failed: {even}"
```
The function `sort_even` takes a list `lst` as input and returns a new list `even` that contains elements from `lst` that are even numbers. The function then returns a list `lst'` that contains all other elements from `lst` that are odd numbers.