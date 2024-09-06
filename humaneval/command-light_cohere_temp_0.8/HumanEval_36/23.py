Here is a self-contained Python script with a function that solves the problem you provided:

```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    count_zero_seven = 0
    result = 0
    
    for num in range(2, n + 1):
        num = str(num)
        if num == "77" or num % 11 == 0 or num % 13 == 0:
            count_zero_seven += 1
        
        if count_zero_seven == 2:
            result += 1
            count_zero_seven = 0
            
    return result

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3)
```

This Python code defines a function `fizz_buzz` that counts the frequency of the number 7 in a sequence of integers less than or equal to a given number `n`. The function iterates through the numbers from 2 to `n`, converting each number to a string, and checking for the occurrence of the number 7. It also counts if the count_zero_seven is 2, it adds 1 to the result and resets count_zero_seven to zero. This process repeats until reaching thelectricity is valid.