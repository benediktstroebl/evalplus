```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i
    return 1  # return 1 if no number divides n

# Tests
assert largest_divisor(15) == 5
assert largest_divisor(18) == 9
assert largest_divisor(21) == 3
```
This script defines the `largest_divisor` function and asserts the function's results against test cases. 
Please note that the `largest_divisor` will return the value `1` if no number divides `n` evenly. 
This is consistent with the directive to return the largest divisor, as `1` is the largest possible divisor of any number. 
If you prefer to treat `1` as not a divisor for the sake of the problem, we can adjust the script accordingly. 

Let me know if you have any more questions or comments on this solution!