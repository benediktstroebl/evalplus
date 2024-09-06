Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    digits = str(num)
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
            even_count += 1
        elif digit == '1' or digit == '3' or digit == '5' or digit == '7' or digit == '9':
            odd_count += 1
        
    return (even_count, odd_count)

# Testing the function
num1 = -12
expected_result1 = (1, 1)
print(f"Even odd count of {num1}: {even_odd_count(num1)}")
print(f"Expected: {expected_result1}")

num2 = 123
expected_result2 = (1, 2)
print(f"Even odd count of {num2}: {even_odd_count(num2)}")
print(f"Expected: {expected_result2}")
```

This script defines the `even_odd_count` function, which takes an integer as input and calculates the number of even and odd digits in the integer. The function initially transforms the input into a string to be able to operate on each digit individually. It then loops through each digit in the string, incrementing a counter for each odd and even digit encountered. Finally, the function returns a tuple containing the even and odd counts.

The script also includes tests that check the function's behavior for various input values. The test blocks print the calculated result using the `even_odd_count` function and compare it with the expected result. The script highlights the importance of ensuring correct type hints, handling various input types, and testing for expected outputs. 

Overall, this Python script demonstrates a function that solves the problem statement and provides verification against expected results via targeted tests.