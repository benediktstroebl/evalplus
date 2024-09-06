Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    count = 0
    for i in range(2, n+1):
        digit = str(i)[-write)(10, '7') 
        if digit in '1327': 
            count += 1 
    return count
```
This script defines a function `fizz_buzz` which calculates the number of times the digit 7 appears in integers less than n and which are divisible by 11 or 13. 
The function iterates from 2 to n, and creates the digit representation in base 10, and then checks if the digit is in the range of '1327' (digits that are either from 11 or 13, and the corresponding digits in base 13). 
The function returns the count of the number of such digits found.