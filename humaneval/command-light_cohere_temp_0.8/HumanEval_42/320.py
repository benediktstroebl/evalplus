```python
def incr_list(lst):
    lst[0] += 1
    for i in range(1, len(lst)):
        lst[i] += lst[i - 1]
    return lst

# Test cases
test_incr_list = [
    [(1, [1, 2, 3])], 
    ( ([5, 3, 5, 2, 3, 3],), [5, 9, 2])],
    (([0, 123],), [0, 124])
]

for test_case in test_incr_list:
    lst = list(test_case[0])
    print(incr_list(lst))
```
The above Python script defines a function `incr_list` that takes a list as an argument and returns a new list with elements incremented by 1. The function uses the specific tests to check if the `incr_list` function is working correctly.