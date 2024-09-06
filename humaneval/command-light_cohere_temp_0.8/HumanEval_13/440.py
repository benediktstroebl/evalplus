```python
def greatest_common_divisor(a, b): 
    while b != 0:
       DELTA = b 
        b = a % b 
    return DELTA
# Test the function
 assert greatest_common_divisor(3, 5) == 1
 assert greatest_common_divisor(25, 15) == 5
 ```