```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list of numbers
test_list = [
    -1, 2, -4, 5, 6, 7, -3, 3, 9, 0, 123, 1, -10
]

res = get_positive(test_list)
print(res)  # Expected output: [2, 5, 6, 3, 9, 123, 1]
```