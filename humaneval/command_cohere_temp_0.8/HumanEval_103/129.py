Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer, then convert it to binary.
    
    Args:
    - n (int): the starting integer.
    - m (int): the ending integer.
    
    Returns:
    - str: Binary string representation of the rounded average if n is not greater than m, 
          otherwise returns -1.
    """
    # Ensure n is not less than m to avoid errors
    if n > m:
        return -1
    
    total = 0
    num = n
    count = 1
    while num <= m:
        # Add num to the total
        total += num
        # Increment count
        count += 1
        # Move to the next number
        num += 1

    # Calculate the average
    average = total / count
    # Round to the nearest integer
    rounded_average = round(average)
    
    # Convert to binary
    binary_representation = bin(rounded_average)[2:]
    return binary_representation if rounded_average != -1 else '-1'

# Test Cases
print(rounded_avg(1, 5))  # Should print "0b11"
print(rounded_avg(7, 5))  # Should print -1
print(rounded_avg(10, 20))  # Should print "0b1111"
print(rounded_avg(20, 33))  # Should print "0b11010"
```

This script has a function `rounded_avg` that takes two integers as input and returns the binary representation of the rounded average of the two integers if the starting integer is not greater than the ending integer. Otherwise, it returns `-1`. This is done using a while loop that adds the integers to a total and increments a count, then calculates the average after the loop. The answer is then rounded and converted to binary.