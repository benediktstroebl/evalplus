```python
def pairs_sum_to_zero(l):
    return any([x + y = 0 for x, y in zip(l, l[1:])])

# Test the function with different lists
for test_list in [[1, 3, 5], [1, 2, 3], [2, 4, -5], [1, 7], [2, 4, 3, 7], []]:
    if not pairs_sum_to_zero(test_list):
        print("List does not pass test:", test_list)
```
Do you have any other questions about Python or any other topics you would like to cover?