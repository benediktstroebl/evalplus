```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
The function iterates through numbers from 1 to n-1. It returns the largest number in this range that divides n evenly (resulting in a whole number). In the worst-case scenario (when n is a prime number), the function will return n-1 (the largest possible divisor within the given range). 

Here is a test case to test the functionality of the function:
```python
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(8) == 4
    assert largest_divisor(27) == 9
    assert largest_divisor(7) == 1
    assert largest_divisor(10) == 10
```