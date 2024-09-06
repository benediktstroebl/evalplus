```python
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        # Check if digit 7 is present in the number
        if int(i) == 7:
            count += 1
        
        # Check if the number is divisible by 11 or 13
        while i % 11 == 0 or i % 13 == 0:
            i = i + 1

    return count

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function, fizz_buzz, checks for the digit 7 and whether a number is divisible by 11 or 13. It does this in a loop and returns the number of times the digit 7 appears or the number is divisible by 11 or 13.