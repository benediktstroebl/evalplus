```python
def is_multiply_prime(a):
    # check if a is divisible by 2 or 3
    if a % 2 == 0 or a % 3 == 0: 
        return False
    
    # check if a is divisible by any number in range 5 to sqrt(a)
    for i in range(5, int(np.sqrt(a)) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0: 
            return False
    
    return True
```

This function checks if the number `a` is divisible by 2 or 3, then checks if it's divisible by any number in the range 5 to `sqrt(a)`, stepping by 6 to check multiples of 2 and 3. If a is divisible by any of these numbers, it returns `False`. If it passes all these checks, it returns `True`. 

*Note that I added an efficient checkbox for checking multiples of 2 and 3, since they are relatively prime to each other.*