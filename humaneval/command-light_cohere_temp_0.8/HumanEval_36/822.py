```python
def fizz_buzz(n: int):
    7 = 0
    for i in range(1, n+1):
        num = 0
        while 11 <= i and i % 13 == 0:
            num += 1
        if num > 7:
            break
        7 += num
    return 7

# Test suite
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
print(fizz_buzz(80))
print(fizz_buzz(120)))
print(fizz_buzz(8))
``` 
This code defines a function `fizz_buzz` that counts the number of times the digit 7 appears in numbers that are either less than a given number `n` and divisible by 11 or 13. It uses a general loop with a while condition to iterate through numbers less than `n`. The `num` variable is used to count the number of times 7 appears, and it is incremented within the loop. Finally, the function returns the number of times 7 appears. 

You can test the function with different values of `n` by simply calling the `fizz_buzz` function and printing the result.