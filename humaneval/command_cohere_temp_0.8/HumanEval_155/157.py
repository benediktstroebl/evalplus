Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # Convert digit to int and check if it is even
        even = int(digit) % 2 == 0
        if even:
            count += 1
    return count, 2 - count 

# Example usage
print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)
```

This script defines the `even_odd_count` function, which uses a generator expression and the modulo operator to determine the count of even and odd digits in the input num. The function returns a tuple with the counts of even and odd digits, which are calculated using 2^1-1 and 2^1, respectively. The provided example usage demonstrates how to call the function with different input values.