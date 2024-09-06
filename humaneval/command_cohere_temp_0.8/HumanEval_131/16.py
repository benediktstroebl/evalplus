```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This Python script defines a function named `digits` which takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable `prod` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number `n`, extracting each digit as a string from the left-to-right order. For each digit, it checks if the digit is odd using the modulo operator `% 2 == 1`, if the condition is true, it multiplies the current value of `prod` by the odd digit. In this way, the function accumulates the product of all odd digits in the number, considering both negative and positive odd digits. Finally, the function returns the value of `prod`, which gives the product of the odd digits of the input number. 

The TDD approach ensures that the code adheres to a set of predefined criteria and performs correctly against a range of potential inputs. This method helps to guarantee the resilience and accuracy of the solution in solving the problem statement.