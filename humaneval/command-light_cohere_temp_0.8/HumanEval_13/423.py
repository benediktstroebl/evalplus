```python
def greatest_common_divisor(a, b): 
    if not divisible(a, b): 
        return 0
    max_div, i = divisor(a, b)
    while i <= max(divisor(a, b) ,divisor(b, a)): 
        if a % i == 0 and b% i ==0: 
            return i 
    return -1 

def divisor(a, b): 
    for i in range(1, min(a, b)+1): 
        if a % i == 0 and b % i == 0: 
            return i 

if __name__ == "__main__": 
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(56, 23) == 23
    assert greatest_common_divisor(2, 56) == 28
    assert greatest_common_divisor(100, 50) == 50
```  The greatest common divisor (gcd) of two integers a and b is computed by the function `greatest_common_divisor`. 

This script provides a function that accepts two integers and returns the greatest common divisor of the two numbers. The function utilizes the  a helper function `divisor` that finds all divisors of the smaller number. The function loops through the all divisors of the smaller number and checks if the larger number is divisible by it.  Finally, the largest divisor is returned.