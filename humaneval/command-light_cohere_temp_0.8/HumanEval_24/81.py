```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 2 + 1
  ```
This function takes an integer n and returns the largest even divisor of n, ensuring that the result is always less than n. 

The function uses the condition n % 2 == 0 to check if n is even, and returns n // 2 in that case. If n is odd, the function returns n // 2 + 1, which is the largest odd divisor of n while ensuring the result remains less than n. 
This approach is self-contained and efficient, as it only involves basic arithmetic operations and a simple condition check.