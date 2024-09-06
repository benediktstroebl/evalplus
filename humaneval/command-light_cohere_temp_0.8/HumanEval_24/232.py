```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if any(divisible(i, n) ))
 
def divisible(num: int, dividend: int) -> bool:
    return (num != 1) and (num * dividend // n == dividend)
 
# Unit tests
test_largest_divisor = []
for i in range(15):
    test_largest_divisor.append(largest_divisor(i))
assert test_largest_divisor == [5]  # Should be true
```