```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    cnt = 0
    for i in range(1, n+1):
        digit = str(i % 10)
        if digit == '7':
            cnt += 1
        if (i % 11 == 0 or i % 13 == 0):
            break
    return cnt
``` 
The function fizz_buzz calculates the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. It does this by iterating through the numbers from 1 to n, checking if the current number has the digit 7. If it does, the digit is 7, the counter is incremented, and if the number is divisible by 11 or 13, the iteration is terminated early. 

This function can be easily used, tested, and understood without relying on external code or additional explanations.