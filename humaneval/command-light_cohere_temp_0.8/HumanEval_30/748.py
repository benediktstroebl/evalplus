```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Example: Get positive numbers from a list
result = get_positive([10, -20, 30, -40, 50])
print(result)  # Output: [10, 30, 50]
```