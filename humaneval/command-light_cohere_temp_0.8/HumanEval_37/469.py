```python
def sort_even(l: list):
    """Sorts a list l such that all even indices are sorted with equal values, while odd indices are sorted to their original values."""
    return sorted(l, key=lambda x: x % 2)

#Test cases
test_list = [1, 2, 3]
print(sort_even(test_list))  # Expected: [1, 2, 3]
test_list = [5, 6, 3, 4]
print(sort_even(test_list))  # Expected: [3, 6, 5, 4]
```  This script defines a function `sort_even` that takes a list as input and sorts it based on the condition that even indices are sorted with equal values, while odd indices are sorted to their original values.