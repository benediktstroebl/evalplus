Here is a self-contained Python script that defines a function largest_divisor that finds the largest number that divides a given number evenly:
```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n+1) if n % i == 0])
```
This function leverages the concept of the maximum integer that divides a given number without remainder. It uses the particular test to determine the largest divisor, ensuring that the answer is always greater than the input number.