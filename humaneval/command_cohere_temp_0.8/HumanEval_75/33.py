```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 3:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if a % i == 0:
            return False
    return True
```

This function checks if the number `a` is divisible by any integer between 2 and the square root of `a`. 

Then, it also checks if the number `a` is divisible by any integer in the list `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]`. 

If none of these conditions are met, the function returns `True`, otherwise it returns `False`. 

Let's break down the code:
- The function starts by checking if the given number `a` is less than 3. In that case, it returns `False` because no number less than 3 can be multiplied by three prime numbers. 
- The function then starts looping through the numbers from 2 to the square root of `a`. This is because it needs to check if `a` is divisible by any number up to its square root, as any factor of `a` larger than the square root would have a corresponding factor smaller than the square root. 
- While looping, it checks if `a` is divisible by any number in the given list of primes. If any of these conditions are met, it returns `False`. 
- If none of these conditions are met, the function returns `True`. 

This problem allows multiple approaches, and this is just one of them. The main idea is to check if the number has any factors which aren't prime.