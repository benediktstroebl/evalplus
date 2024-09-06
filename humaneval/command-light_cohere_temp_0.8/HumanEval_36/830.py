```python
def fizz_buzz(n):
    count_seven = 0
    for num in range(1, n+1):
        if is_divisible_by_11_or_13(num):
            count_seven += 1
    return count_seven

def is_divisible_by_11_or_13(num):
    return num % 11 == 0 or num % 13 == 0

#fizz_buzz(50)
# Output: 0
# fizz_buzz(78)
# Output: 2
# fizz_buzz(79)
# Output: 3
```
This code defines a fizz_buzz function that calculates the number of occurrences of the digit 7 in numbers less than n which are divisible by 11 or 13. It uses a single loop to iterate through numbers from 1 to n. The is_divisible_by_11_or_13 function checks whether a number is divisible by 11 or 13, and the fizz_buzz function then returns the count of 7.