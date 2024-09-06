```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the decimal part of the number. 

To test this function, you can call it with a float input and assert that the output is less than 1:
```python
import numpy as np

def test_truncate_number():
    # Arrange
    number = 3.5

    # Act
    result = truncate_number(number)

    # Assert
    assert result < 1
    assert isinstance(result, float)

test_truncate_number()
```

This will assert that the output is less than 1 and that the function returns the correct type.