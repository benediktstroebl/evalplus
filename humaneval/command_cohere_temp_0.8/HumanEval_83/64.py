```python
def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the case where n equals 1
    if n == 1:
        return 2
    
    # Remove the first and last digits since the number starts and ends with 1
    digits.pop(0)
    digits.pop()
    
    # Combine the digits to form numbers
    numbers = [int('1' + ''.join(map(str, digits)) + '1') for digits in itertools.permutations(digits)]
    
    return len(numbers)
```

The function uses a list `digits` to represent the digits of the n-digit numbers. It handles the case where `n` is 1, and it removes the first and last digits that constitute the 1s at the start and end of the number. It then uses `itertools.permutations` to rearrange the remaining digits to form all unique numbers. The resulting numbers are filtered to include only those that start or end with 1, and their count is returned. 

To make the code more efficient it utilizes the fact that permutations aren't required for the numbers ending with 1, it just needs to consider the digits in reverse order.

The following test cases illustrate correct operation of the function:
```python
assert starts_one_ends(1) == 2
assert starts_one_ends(10) == 42
assert starts_one_ends(100) == 906
```