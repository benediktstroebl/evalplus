```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid")
    elif not (a % b == 0) or b == 0:
        raise ValueError("The divisor must be less than the number")
    else:
        return b
  ```