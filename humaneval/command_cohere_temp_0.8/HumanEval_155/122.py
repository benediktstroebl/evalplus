Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is then tested with a test case that verifies its functionality:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    num_str = str(num)
    count_even = 0
    count_odd = 0
    for char in num_str:
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)

# Test Case
print(even_odd_count(-12))  # (-1, 1)
print(even_odd_count(123))  # (1, 2)
```
This script defines the function even_odd_count that takes an integer num as input and follows the steps that are mentioned in the previous response. It calculates the number of even and odd digits from the string representation of the integer and returns a tuple containing them. The test case is also added to demonstrate its functionality.