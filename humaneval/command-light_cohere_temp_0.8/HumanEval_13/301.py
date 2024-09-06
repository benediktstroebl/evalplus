```python
def greatest_common_divisor(a, b): 
    while b != 0:
        a, b = b, a % b 
    return a 

# Test case for 3 and 5
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case for 25 and 15
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This function utilizes the Euclidean algorithm to find the greatest common divisor of two integers a and b. The time complexity of the greatest common divisor using the Euclidean algorithm is O(log(min(a,b)))) and is a well-known method for this problem.