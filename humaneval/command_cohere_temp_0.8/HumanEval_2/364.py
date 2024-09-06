```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than number, which is achieved by flooring the number, from the original number, yielding the residual fraction desired. 

Here are some test cases to ensure the correct functioning of the above function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.0) == 0.0
    assert truncate_number(10.1) == 0.1
    assert truncate_number(0.01) == 0.0
    assert truncate_number(100.05) == 0.05
```
The expected outcome for each test case is provided in rounded brackets '()'.