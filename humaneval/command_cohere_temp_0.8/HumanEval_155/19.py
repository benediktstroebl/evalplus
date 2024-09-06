Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the number
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
            
    return (count_even, count_odd)

# Example usage
print(even_odd_count(-12))  # (1, 1)
print(even_odd_count(123))  # (1, 2)
```

This function takes a integer num as input, counts the number of even and odd digits in num's string representation, and returns a tuple containing these two counts. It thoroughly checks each digit in the number's string representation and categorizes it as either even or odd, ultimately providing the desired result.