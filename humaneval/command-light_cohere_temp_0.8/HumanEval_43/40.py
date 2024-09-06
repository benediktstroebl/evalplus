```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# Test the function with various lists
for test_list in [[1, 3, 5, 0], [1, 3, -2, 1], [2, 4, 3, 7], [1], []]:
    if not pairs_sum_to_zero(test_list):
        print("Failed to find two elements summing to zero.")

```
Do you want me to help you with any other questions related to Python programming or specific tasks?