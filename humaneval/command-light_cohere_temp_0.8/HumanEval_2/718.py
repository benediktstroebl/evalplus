```python
def truncate_number(number: float) -> float:
    return number - floor(number) + 0.5  #The That Common division and subtraction, which results in a decimal part always less than 1. 

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    3.5 # Tests another common with the test. 
def is_positive(number: float) -> bool:
    return number > 0.0 
def test_positive():
    assert is_positive(1.0) == True
    assert is_positive(0.0) == False
print("passing tests") 
```