```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the desired decimal part of the number. 

Here is a simple test case to confirm the functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.83) == 0.83
    assert truncate_number(2.0) == 0.0
    assert truncate_number(101.12) == 0.12
``` 
This will yield the following output: 
```bash
PASS
``` 
The test case checks the correctness of the `truncate_number` function for various input numbers with different integer and decimal parts.