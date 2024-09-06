```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with different lists of numbers
tests = [
    [],
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

for test_list in tests:
    actual_list = get_positive(test_list)
    print(f"Test List: {test_list}")
    print(f"Actual Output: {actual_list}")
    print("="*"*len(actual_list))
    print()
```
This Python code defines a function `get_positive` that filters out and returns only positive numbers from the input list. It uses list comprehension to iterate over each element in the input list and checks if the element is greater than zero, which is a positive number. The function is then passed to a loop with different test lists, and the output is printed.

This code is self-contained and demonstrates how to create a function to solve a specific problem.