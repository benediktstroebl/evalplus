```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: One or both arguments is not a number"
    return max(x for x in range(1, min(a, b) + 1) if a % x == 0 and b % x == 0)

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This Python code defines a function called greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It utilizes an list comprehension to find all numbers from 1 up to the minimum of the two input numbers (min(a, b) + 1) that are both divisors of a and b. In other words, the list comprehension is used to check if a given number divides both a and b without leaving a remainder. 

The function returns the maximum of these common divisors, ensuring that it always returns a valid result for the given inputs.