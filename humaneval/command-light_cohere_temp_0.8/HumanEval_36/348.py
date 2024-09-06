```python
def fizz_buzz(n: int) -> int: 
    result = 0
    for num in range(2, n+1): 
        count = 0
        for i in range(10): 
            if num % i == 0 and i > 7: 
                count += 1 
        if count > 0:
            result += 1 
    return result
``` 
This function, `fizz_buzz`, takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a
 nested loop to iterate through numbers from 2 to `n`, and for each number, it iterates through the digits from 0 to 9. This is digit that divides the number evenly and is greater than 7 is recorded in the `count` variable. Once all such digits that meet these condition have been identified, the function adds 1 to the `result`. Finally, the function returns the value of `result`.