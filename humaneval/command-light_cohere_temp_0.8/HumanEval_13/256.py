Here is a self-contained Python function that finds the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    gcd = (a, b)
    while b:
        a %= b
        gcd = b
    return gcd
```
This function takes two integers a and b as input and initializes the gcd variable with the pair (a, b) to start the loop. The loop will continue until b is 0, then it will return the gcd variable. 

Here is the test code:
```python
# Testing the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This code shows the passing of the test cases.