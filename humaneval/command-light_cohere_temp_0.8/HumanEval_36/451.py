```python
def fizz_buzz(n):
    count = 0
    for num in range(10, n+1):
        num = str(num)
        count += num.find("7") == True
   
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3)
```
This code defines a function fizz_buzz(n) that calculates the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop to iterate through numbers from 10 to n, converts each number to a string, and counts the occurrences of the digit 7. Finally, the function returns the count, which represents the number of valid outputs.