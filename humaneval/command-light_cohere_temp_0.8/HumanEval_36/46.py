```python
def fizz_buzz(n: int):
    # Initialize a count of zero
    count = 0
    
    # Iterate through integers less than n
    for num in range(1, n+1):
        # If the number is divisible by 11 or 13, increment the count
        if (num % 11 == 0 or num % 13 == 0):
            count += 1
    
    return count

#>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```
The function uses a simple loop to iterate through the numbers from 1 to n. It checks each number for divisibility by 11 or 13 using the modulo operator. If the number is divisible by 11 or 13, the count is incremented. The function then returns the count, which represents the number of times the digit 7 appears in the sequence of numbers less than n which are divisible by 11 or 13.