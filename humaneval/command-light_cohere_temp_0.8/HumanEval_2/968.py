```python
def truncate_number(number: float) -> float:
    return max(number) - floor(number) if number.is_integer() else number if number.is_decimal() else 0
```

def is_integer(number: float) -> bool:
    return number != float('inf') and number != float('-inf') and number.isdigit()
floor(number) == number)

def is_decimal(number: float) -> bool:
    return str(number).isdigit() and float(int(number[0])))

def floor(number: float) -> int:
    return int(number)

def test_truncate_number():
    try:
        assert truncate_number(3.5) == 0.5
        print("Test: pass")
    assert is_integer(3.5)
        print("Test: pass")
    assert is_decimal(3.5)
    print("Test: pass")
    assert floor(3.5) == 5
   
    print("Test: pass")
def test_is_integer():
    assert is_integer(0)
    assert is_integer(1)
    assert is_integer(1337)
    assert is_integer(float('inf'))
    assert is_integer(float('-inf'))
    assert not is_integer('abc')

def test_is_decimal():
    assert is_decimal(0)
    assert is_decimal(1)
    assert is_decimal(123456789)
    assert is_decimal(float('abc'))
    assert not is_decimal(float('-123.45'))
def test_floor():
    assert floor(3.5) == 5
    print("Test: pass")

if __name__ == "__main__":
    test_truncate_number()
    test_is_integer()
    test_floor()

```
This script defines a function `truncate_number` that takes a positive number as input and returns the decimal part of the number, rounded down to the nearest integer. The `is_integer` function checks whether a number is an integer, and the `is_decimal` function checks whether a number is a decimal. The `floor` function is used to get the integer part of a number. The `test_truncate_number` function tests whether the `truncate_number` function works correctly, and the `test_is_integer` and `test_floor` functions test whether the `is_integer` and `floor` functions work correctly.