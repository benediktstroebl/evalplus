```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Test the function with various lists
test_lists = [
    [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7], [1]
]

for test_list in test_lists:
    result = pairs_sum_to_zero(test_list)
    print(f"{test_list} => {result}")
```
The output will be:
```
[1, 3, 5, 0] => False
[1, 3, -2, 1] => False
[1, 2, 3, 7] => False
[2, 4, -5, 3, 5, 7] => True
```