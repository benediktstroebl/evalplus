```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 2 + 1
  ``` 
This function will return the largest even positive divisor that is smaller than the number 'n'.