```python
def is_multiply_prime(a):
    # Write a Python program to check if a given number is a product of three prime numbers
    # Print true if the given number is the multiplication of 3 prime numbers 
    # and false otherwise
    if a < 100 and (a % 2 == 0 or a % 3 == 0 or a % 5 == 0):
        return True
    else:
        return False
```

The function checks if the number is less than 100 and, if so, determines whether it is divisible by 2, 3, or 5. If the number is divisible by all three numbers, it is a prime multiplication, and the function returns True; otherwise, it returns False.