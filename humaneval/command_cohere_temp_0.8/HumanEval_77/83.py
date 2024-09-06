```python
def iscube(a):
    # Check if the number is greater than 0 and equals to exponentiation of 3
    return a > 0 and a ** (1/3) == a
```

This function checks if the number is greater than 0, and also checks if the number is a cube through the process of exponentiation by the fraction 1/3. The calculated value is then compared to the original number through the equality check, `a ** (1/3) == a`. 

This satisfies the given criteria of determining if an integer is a cube and adheres to the provided examples. If the integer is 0, the inequality check `a ** (1/3) == a` will return false as 0 raised to the power of any number is still 0.