```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test the function
for i in range(0, 5):
    if pairs_sum_to_zero([1, i, 3, -i, 7]) == False:
        print(f"Error: {i} does not have two summing integers that add up to zero.")
```