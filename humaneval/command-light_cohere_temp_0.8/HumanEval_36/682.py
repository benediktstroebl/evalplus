```python
def fizz_buzz(n):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, n + 1):
        digit = str(i)[0]
        if digit == 7:
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            break
    
    return count

# Example usage
assertEqual(fizz_buzz(50), 0)
assertEqual(fizz_buzz(78), 2)
assertEqual(fizz_buzz(79), 3)

```
This function uses a for loop to iterate through numbers from 1 to n. It checks each digit in the number, if it's 7, then it counts it as the number of occurrences of 7 in numbers less than n and divisible by 11 or 13, if i is divisible by 11 or 13 at the same time.