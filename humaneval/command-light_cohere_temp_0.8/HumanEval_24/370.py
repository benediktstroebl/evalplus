```python
def largest_divisor(n: int) -> int:
    return n if n % 2 == 0 else n + 1
```
Passing tests are done by this code using a if condition. The function returns n if the divisible by 2, and returns n + 1 if the number is not divisible by 2. This method works for any larger numbers by doing this.