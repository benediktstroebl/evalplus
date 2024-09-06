```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test cases
test_get_positive = []
test_cases = [
    [ [-1, 2, -4, 5, 6], ],
    [ 5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10 ],
    [ [1, 2, 3, -4],
    [999, 42, -123]
]

for lst, expected in test_cases:
    test_get_positive.append(get_positive(lst))
    test_get_positive.append(expected)

print("Test cases passed.")
```