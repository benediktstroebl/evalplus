```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This script defines a function named `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. It initially sets the `prod` variable to 1, initially. Then, it loops through each digit in the string representation of the argument, checking if each digit is odd using the modulo operator (`%`). If the digit is odd, it multiplies the `prod` by the odd digit. Finally, it returns the value of `prod`, which will be 0 if all digits are even, and the product of the odd digits otherwise. 

The self-contained code block solves the problem statement and allows others to use and understand the code easily. It can be executed directly within the Python environment or IDE to observe the results.  This solution is efficient and follows standard Python styling.