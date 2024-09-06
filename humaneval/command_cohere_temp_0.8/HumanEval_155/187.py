Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple containing the counts of odd and even digits in num. This function is further explained through an example execution:
```python
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    
    # Iterate through each digit in the integer representation
    for digit in num_str:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return (count_even, count_odd)

# Example execution
print(even_odd_count(123))  # This should output (1, 2)
```

The function leverages Python's str data type to convert the integer parameter into a string, allowing individual digit access through iteration. For each digit, it checks if the digit is even or odd using the modulo operator (`%`). Subsequently, the function maintains separate counts of even and odd digits and returns them as a tuple.

To ensure the functionality, test your code with different inputs to verify the correctness of the function.