```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of truncation. 

To test this function, you can call it with a float input and compare the output to the expected value:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.1),
    (1.5, 0.5),
    (1.0, 0.0),
    (0.5, 0.0),
    (0.1, 0.0)
]

for number, expected in test_cases:
    actual = truncate_number(number)
    assert actual == expected
```
Alternatively, you can verify the correctness of the function by checking that the output from the following code is consistent with the expected output.
```python
>>> truncate_number(3.5)
0.5
```
Please note that in the test code, the `assert` statement will raise an error and execution will halt if the condition evaluates to False, i.e., if the actual output of `truncate_number` does not match the expected output. Thus, this code effectively tests the correctness of the function `truncate_number`.