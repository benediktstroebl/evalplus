```python
def sort_third(l: list):
    """Sorts a list so that values not divisible by three are at the front, and the other values are at the back"""
    l = list(sorted(l, key=lambda x:int(x) % 3 == 0))
    return l

# Test cases
print(sort_third([1, 2, 3]))  # Expected Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected Output: [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 2, 13, 19, 3, 97, 97]))  # Expected Output: [97, 97, 19, 13, 2, 10, 3]
```