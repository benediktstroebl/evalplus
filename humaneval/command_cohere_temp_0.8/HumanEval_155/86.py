Here's a Python script that contains a function called even_odd_count which takes an integer num as its input and returns a tuple with the counts of even and odd digits in num, as described in the problem:
```python
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the input number
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return (count_even, count_odd)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

This script defines the `even_odd_count` function, which uses a string representation of the input number to iterate through each digit with a simple loop. It keeps track of even and odd digits using the count_even and count_odd variables, respectively, and finally returns the counts as a tuple. The example usage demonstrates how the function works for different input numbers.