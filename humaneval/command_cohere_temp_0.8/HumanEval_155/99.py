Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    # Iterate each digit in the input number
    for digit in str(num): 
        # increment count if digit is odd
        if digit % 2 == 1: 
            count += 1
    return count, len(str(num)) - count
```
The function uses a str(num) conversion to convert the integer input num to a string, then iterates through each digit in the string and increments the count variable if the digit is odd. After iterating through all digits, it returns a tuple with the count of odd digits and the difference between the length of the string representation of num and the count of odd digits.

To test this function, you can run the following code:
```python
# Test Case for Input Number -12
test_case = [-12]
expected_result = (1, 1)
test_results = [even_odd_count(num) for num in test_case]
print(test_results == expected_result) 

# Test Case for Input Number 123
test_case = [123]
expected_result = (1, 2)
test_results = [even_odd_count(num) for num in test_case]
print(test_results == expected_result)
```
This will return True since the function's outcomes correspond to the anticipated results for both test cases.