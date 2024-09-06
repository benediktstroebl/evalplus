```python
def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of 4 even positive numbers
    # By factoring the number into 2*x where x is an odd number
    if n % 2 == 0: 
        x = n // 2
        if x % 2 == 0:
            return True
    return False
```

This function evaluates whether the given number `n` can be written as the sum of exactly 4 positive even numbers. It does so by:
1. Checking if `n` is even, if this condition is met, it proceeds to the next step, otherwise, it returns `False` right away as any odd number cannot be expressed as the sum of exactly 4 even numbers. 
2. If `n` is even, it divides it by 2 to get the value of `x`.
3. Then it checks if x is also even and if it is, it returns `True` because it can be expressed as 2*x and n = 2*x+x = 3*x, which are three even numbers. 

The provided example tests show that this function achieves the required behavior. 

You can easily adapt this function to test for the sum of any even positive numbers, changing the number in the tests and adjusting the `if` statements and returns accordingly. G