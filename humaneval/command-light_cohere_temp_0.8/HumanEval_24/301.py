```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

#Test case 1:
assert largest_divisor(15) == 5

#Test case 2:
assert largest_divisor(10) == 2

#Test case 3:
assert largest_divisor(3) == 3

#Test case 4:
assert largest_divisor(1) == 1

#Test case 5:
assert largest_divisor(18) == 6
```