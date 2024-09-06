```python
def truncate_number(number: float) -> float:
    return round(number) // 10

def test_truncate_number():
    number = float('3.5')
   
    assert truncate_number(number) == 0.1

def round(number: float) -> float:
    """ Rounds a floating point number to the nearest integer, and returns the integer part."""
    return int(number)

def test_round():
    number = float('3.4')
    assert round(number) == 3.2

if __name__ == "__main__":
    test_truncate_number()
    test_round()
```
The script defines a function round that rounds a number to the nearest integer and then returns the integer part. It also defines a test_round function with an assertion that checks if the result of round is correct for the given number 3.4.  It test for the is a simple way to check that a function is working correctly.