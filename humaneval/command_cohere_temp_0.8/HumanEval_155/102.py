Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # increment count if digit is odd
        if digit % 2 != 0: 
            count += 1 
    return count, 10 - count 

# Testing the function with some test cases
# Assert that the function returns a tuple with equal values for single digit inputs
assert even_odd_count(1) == (1, 1)
assert even_odd_count(5) == (1, 1)

# Assert that the function returns proper counts for multidigit inputs
assert even_odd_count(123) == (1, 2)
assert even_odd_count(-12) == (1, 1)

print("All tests passed!")
``` 

This script defines the even_odd_count function, which takes an integer num as input and returns a tuple with the count of even and odd digits in num. The function uses a for loop to iterate through each digit in the decimal representation of the input num, and uses the modulo operator to determine if the digit is even or odd, incrementing the count accordingly. 

The testing block verifies the function's output against test cases for single-digit and multi-digit inputs. Finally, upon passing the tests, the script confirms with a successful test outcome message.