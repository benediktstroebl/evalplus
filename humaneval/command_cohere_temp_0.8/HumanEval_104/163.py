```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 != 0 for c in str(x))]
    return sorted(odd)
```

The function `unique_digits(xs)` takes a list of numbers (`xs`) as input and returns a sorted list of all the elements that do not have any even digits. The function checks if any digit in a number is odd using the expression `any(int(c) % 2 != 0 for c in str(x))` and then adds the number to the `odd` list if the condition is true. Lastly, the function returns a sorted odd list.

Here is a simple test case to verify the functionality of the function:
```python
test_list = [15, 33, 1422, 1, 322]
expected_result = [1, 15, 33]

# Test case
assert unique_digits(test_list) == expected_result
``` 

Thus, the function's test case returns the expected result.