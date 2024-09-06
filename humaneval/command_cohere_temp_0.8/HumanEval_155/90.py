Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    count = 0
    for digit in str(abs(num)):
          if int(digit) % 2 == 0:
            count += 1
    return count
```
The function uses a loop to iterate through the digits of the string representation of the absolute value of the input number. It counts the number of even digits and returns the result.

Here is a test to call the function directly with different numbers to test its functionality:
```python
test_cases = [
            (-12, (1, 1)),
            (123, (1, 2)),
            (10, (1, 0)),
            (515, (0, 1)),
            (15, (1, 1)),
            (0, (0, 0)),
            (21, (0, 1)),
            (149, (1, 2)),
            (988, (2, 1)),
]

for num, expected in test_cases:
    result = even_odd_count(num)
    assert result == expected
```
The test_cases list contains tuples of input numbers and the expected results from the function. By using python's assert function, we check if the output from the function is correct.

The full code is assembled as follows:
```python
def even_odd_count(num):
    count = 0
    for digit in str(abs(num)):
          if int(digit) % 2 == 0:
            count += 1
    return count

test_cases = [
            (-12, (1, 1)),
            (123, (1, 2)),
            (10, (1, 0)),
            (515, (0, 1)),
            (15, (1, 1)),
            (0, (0, 0)),
            (21, (0, 1)),
            (149, (1, 2)),
            (988, (2, 1)),
]

for num, expected in test_cases:
    result = even_odd_count(num)
    assert result == expected
```