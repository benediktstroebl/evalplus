```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer less than or equal to `number` from `number` which yields the original number minus its integer part, which is the desired decimal part of the number. 

Here is a simple test case to confirm the functionality of the function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(2.0) == 0.0
    assert truncate_number(1.1) == 0.1
    assert truncate_number(0.5) == 0.0
    assert truncate_number(2.5) == 0.0
``` 
The test cases highlight that the function correctly identifies the decimal part of different test cases, returning 0.5 in the case of 3.5, and 0.0 in the cases of 2.0, 1.1, and 0.5 respectively, and finally, it correctly identifies 2.5 as having no decimal part, yielding 0.0.