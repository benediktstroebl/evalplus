```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. 

To test this function, here is a code block with its corresponding test:
```python
test_truncate_number = 3.5
expected_result = 0.5
result = truncate_number(test_truncate_number)
assert result == expected_result
```

Thus, this should return `True` as the test's result execution. 
```python
result = truncate_number(3.5)
print(result)
```
This would print `0.5` as the result of the execution.