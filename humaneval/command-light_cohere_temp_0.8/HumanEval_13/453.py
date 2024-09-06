```python
def greatest_common_divisor(a, b): 
    if not(a == 0): 
        return 0
    elif b == 0:
        return 1
    else:
        return greatest_common_divisor(b%a, a) + 1
  ```