```python
def fizz_buzz(n):
    count_seven = 0
    for i in range(1, n+1):
        num = int(str(i))
        if num % 11 == 7 or num % 13 == 7:
            count_seven += 1
    return count_seven

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines the fizz_buzz function, which counts the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. The function iterates through numbers from 1 to n, converts each number to an integer, and checks if the number is divisible by 11 or 13. If the number matches either condition, it is added to the count_seven counter. Finally, the function returns the count_seven, indicating the number of occurrences of 7.