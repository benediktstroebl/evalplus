```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension, filtering out elements that are not greater than zero. This allows it to return a list containing only the positive numbers from the input list. 

To test this function, you can use the following:
```python
test_list = [-1, 2, -4, 5, 6]
expected_result = [2, 5, 6]

assert get_positive(test_list) == expected_result
```

The function should return the expected result, which is [2, 5, 6].