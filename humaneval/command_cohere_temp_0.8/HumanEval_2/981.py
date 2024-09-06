```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer less than or equal to `number` from `number`, which yields the original number minus its integer part, which is the decimal part of the original number. 

Here is a simple test suite for this function:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.7) == 0.7
    assert truncate_number(2.0) == 0.0
    assert truncate_number(10.2) == 0.2
    assert truncate_number(1.1) == 0.1
    assert truncate_number(99.99) == 0.99
``` 

This test suite contains a test for a variety of cases, ensuring that the function behaves correctly for both whole numbers and numbers with decimals. 

To run these tests, you can simply call the `test_truncate_number` function in your Python environment. 

Let me know if I can be of further assistance!