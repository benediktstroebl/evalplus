```python
def largest_divisor(n):
    """ Returns the largest divisor of n <= n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through factors of `n` in the range of `1` to `n` and returns the largest factor that yields a remainder of zero when divided by `n`. This can be better understood using the following example:
```python
largest_divisor(16) # 16 / 2 = 8 -> 16 % 2 == 0
largest_divisor(17) # 17 / 2 = 8 -> 17 % 2 != 0
largest_divisor(24) # 24 / 2 = 12 -> 24 % 2 == 0
largest_divisor(25) # 25 / 2 = 12 -> 25 % 2 != 0
```
In the above example, for the numbers 16, 24, and 25, the function returns the largest divisor which is `2`. It is important to note that the output `8` for the input `16` is not considered a divisor as it is greater than the input number `16`. 

This is because the function is designed to find the largest divisor that is smaller than or equal to the input number. 

Feel free to ask any questions if you'd like further clarification!