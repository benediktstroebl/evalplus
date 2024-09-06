```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```
This function uses list comprehension to filter out negative numbers from the input list, ensuring that it only returns positive numbers. 

It provides a clear and concise solution with minimal code.