```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function takes a positive integer `n` as input and calculates the product of its odd digits. It converts the input number `n` to a string to iterate through its digits. For each digit, if it is odd, the code multiplies it with the `prod` variable, which should be initially 1 and is used to accumulate the product of odd digits. Finally, the function returns the resulting product of odd digits, or 0 if all digits are even. 

Here is a test case to test the functionality of the script:
```python
test_cases = [
    (1, 1),
    (4, 0),
    (235, 15),
    (123, 21)
]

for n, expected in test_cases:
    produced = digits(n)
    assert produced == expected
``` 

The unit test checks if the output of the function corresponds to the expected product of odd digits for each test case. 

This problem can be solved in different ways and this is an example of one possible solution.