```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which leaves us with the leftover fraction (the decimals), hence, solving the problem. 

To test this function, you can call it with a floating point input and compare the output to the expected value. 
For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.1),
    (1.5, 0.5),
]
for num, expected in test_cases:
    assert truncate_number(num) == expected, f"For {num}, expected {expected}, got {truncate_number(num)}"
```
The test suite consists of a list of tuples where each tuple consists of the input number and the expected decimal part. The `assert` statement checks if the output of the `truncate_number` function is equal to the expected value. If they are not equal, the test fails and prints an error message.