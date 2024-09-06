Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input num is not of type int")
    
    digits = str(num)
    even_count = 0
    odd_count = 0
    
    for digit in digits:
        if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
            even_count += 1
        elif digit == '1' or digit == '3' or digit == '5' or digit == '7' or digit == '9':
            odd_count += 1
        
    return (even_count, odd_count)

# Example usage:
num1 = -12
result1 = even_odd_count(num1)
print(f"Even and odd digit count of {num1}: {result1}") 

num2 = 123
result2 = even_odd_count(num2) 
print(f"Even and odd digit count of {num2}: {result2}") 

```
This script will output:
```
Even and odd digit count of -12: (1, 1)
Even and odd digit count of 123: (1, 2)
```
The function has also been updated to handle the edge case of non-integer input, rejecting them with a ValueError.