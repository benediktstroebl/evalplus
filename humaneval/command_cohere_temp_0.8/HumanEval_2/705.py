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
    (7.1, 0.1),
    (9.5, 0.5)
]
for number, expected in test_cases:
    assert truncate_number(number) == expected
```
If this script runs successfully, it will indicate that the function behaves as expected.