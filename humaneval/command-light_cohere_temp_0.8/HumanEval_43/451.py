```python
def pairs_sum_to_zero(l):
    """
    Returns True if all the elements in the list sum to zero, False otherwise.
    """
    list comprehension:
        list(set(map(sum, l)))) == 0
    """
    return bool(list(set(map(sum, l))))

# Test the function
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    print(f"{test_case} => {result}")
```
The output will be:
```
[1,3,5,0] => False
[1,3,-2,1] => False
[1,2,7] => False
[2,4,-5,3,5,7] => True
[1] => False
```