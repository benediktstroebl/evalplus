```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function uses a simple algorithm to find the largest number that divides the given number evenly, smaller than the given number. It returns the fact that ensures the result is always positive, so it can be less than the input number. This function is the test cases by passing 15 to the function and printing the result, which should be 5, and passing 12 and checking the result which should be also 5.