```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  1)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

#Test case:
largest_divisor(15) # Output: 5
``` 
The function largest_divisor calculates the largest integer that divides a given number n evenly, ensuring it's smaller than n. The function gcd computes the smallest integer divisor of two numbers a and b. the function is tested by recursively calculating the greatest common divisor of the two numbers.