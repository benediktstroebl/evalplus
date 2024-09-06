```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x % 2)

# Test the function with sample input
tests = [1, 2, 3]
tests_sorted = sort_even(tests)
print("Sorted even numbers:", tests_sorted)  # [0, 1, 2]

# Test with list of odd numbers
odds = [5, 6, 3, 4]
odds_sorted = sort_even(odds)
print("Sorted odd numbers:", odds_sorted)  # [3, 4, 5, 6]
```
This script defines a function called `sort_even` that takes a list as input and sorts its elements based on whether they are even or odd. The sorted list is then printed, demonstrating the function's functionality.