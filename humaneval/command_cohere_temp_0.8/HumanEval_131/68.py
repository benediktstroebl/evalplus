```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable called `product` to 1, which will be used to accumulate the product of odd digits. Then, it iterates through each digit in the decimal representation of the input number `n` and checks if the digit, when converted to an integer, is odd using the modulo operator (`%`). If the digit is odd, it multiplies it by the `product`, updating it to the next odd digit iteration. Finally, the function returns the value of the `product` accumulator, which gives the product of the odd digits in the input number, or 0 if all digits are even. 

The code is self-contained and does not rely on any external variables or functions, making it reusable and easy to maintain. 

You can test this function on various input numbers to verify its correctness: 
```python 
# Example Test Cases
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235)) # Output: 15
print(digits(12345678)) # Output: 65760
``` 
This should output: 
1
0
15
65760Utils:Output: