```python
def sort_third(lst):
    """Sorts the list lst such that elements which are divisible by three are in their correct position, and other elements are in their original positions.
    Test cases that passing any list of integers.
    """
   
    import list
    """
    return sorted(lst) if all(x%3 == 0 for x in lst) else lst
    """

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [10, 11, 12, 13, 14, 15]
]

# Function calling
for case in test_cases:
    assert sort_third(case) == case
```