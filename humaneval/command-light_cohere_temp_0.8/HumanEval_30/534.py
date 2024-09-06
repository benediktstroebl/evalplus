```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different lists
test_get_positive = []
# Provide your own test cases
for i in range(10):
    test_get_positive.append([i[-i-2], -i])
test_get_positive.append([0])
test_get_positive.append([i, -1])
test_get_positive.append([3, 2, -3])
test_get_positive.append([5, 6])
test_get_positive.append([9, -2, -4, 7])
test_get_positive.append([8, 0, 8, 9])

# Run the function and verify the results
print(f'List: {**test_get_positive**})
print(f'Result: {get_positive(test_get_positive)})
```