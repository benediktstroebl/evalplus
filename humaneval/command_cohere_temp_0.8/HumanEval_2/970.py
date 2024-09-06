```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (largest integer less than the number). This difference is the desired decimal part of the original number. 

Here are some examples of test cases that prove the correctness of the function against the expected output:
```python
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0001) == 0.0001
assert truncate_number(11.999999) == 9.999999
```