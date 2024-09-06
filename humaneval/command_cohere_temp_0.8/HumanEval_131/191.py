```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input integer to a string to iterate through its digits. For each odd digit (ones with a digit counting value of 1), it multiplies this digit with the `product` variable, which starts at 1 and updates by multiplying with each odd digit encountered. Finally, it returns the resulting product of odd digits. 

The TDD approach ensures we've created a function that meets expectations for different scenarios, including edge cases. Feel free to ask any follow-up questions or request further refinements!