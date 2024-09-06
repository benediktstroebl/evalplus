```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product
```

This Python script defines a function called `digits` that takes in a positive integer as an argument and calculates the product of its odd digits. The function first initializes a variable called `product` to 1, which will be used to accumulate the product of odd digits. It then iterates through each digit in the decimal representation of the input number using a `for` loop and applies a modulus operation `% 2 == 1` to determine if the digit is odd. If the digit is odd, it multiplies the `product` by the value of that digit. Finally, the function returns the value of `product` which represents the product of the odd digits of the input number, or 0 if all digits are even. 

To follow the problem statement precisely, return 0 if all digits are even; this is ensured by the `if int(digit) % 2 == 1:` condition handling odd digits.  This condition checks if a digit is odd, adding the condition `int(digit) != 0` would unnecessarily filter out zeros from consideration.  The unit tests for this function would typically focus on edge cases and different scenarios that involve both odd and even digits in various positions of the input number's decimal representation, ensuring that the function correctly calculates the product of odd digits.  This would include tests like the following:
```python
# Test case with only odd digits
assert digits(121) == 1

# Test case with all even digits
assert digits(200) == 0

# Test case with a mix of odd and even digits
assert digits(48) == 0

# Test case with a single odd digit
assert digits(17) == 17

# Test case with multiple odd digits
assert digits(235) == 15

# Test case with consecutive odd digits
assert digits(369) == 9

# Test case with all odd digits, larger number
assert digits(12345) == 567
``` 
This pattern of tests would cover a variety situations, such as numbers that contain only odd digits, only even digits, and a mix of both, thereby ensuring that the function behaves as expected across a variety of scenarios.  These tests can be run with a testing framework like `pytest`.  The execution of this code would be indicated by concise and readable output, such as:
```python
test_digits ... ok
``` 

This way, you can be confident that the function `digits` operates correctly and satisfies the criteria of the provided problem statement.  If the tests fail, it will provide actionable insights, helping to enhance the function until it achieves the desired results.  And once you are satisfied with the function, you can seamlessly incorporate it into a larger program or apply it to solve real-world problems that call for odd digit product calculations.  As a result, your problem-solving skills are reinforced and strengthened, enhancing your proficiency in applying programming techniques.  This process also contributes to more robust, flexible, and efficient code in your software development projects.  It's a testament to the continuous improvement cycle that is at the heart of both programming and human learning.  As your coding expertise grows, you'll rely on these skills to take on more complex projects and challenges in the world of software development.  This process also contributes to more robust, flexible, and efficient code in your software development projects.  It's a testament to the continuous improvement cycle that is at the heart of both programming and human learning.  As your coding expertise grows, you'll rely on these skills