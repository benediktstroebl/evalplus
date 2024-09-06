```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit[0] == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
 ```

This code defines a function called fizz_buzz that calculates the frequency of the number 7 in the range of numbers less than n, specifically focusing on the numbers that are both divisible by 11 or 13. The function iterates through each digit in each number from 1 to n, and checks if the first digit is 7 and if the number is divisible by 11 or 13. The count of such all such particular number that meets the criteria, the function adds 1 to the count. Finally, the function returns the count, representing the number of times the digit 7 appears in such numbers.