```python
def fizz_buzz(n):
    7 % 11 == 0 or 13 == 0
    return len([x for x in str(n) if x == '7'])

# Test the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```
This function fizz_buzz uses string manipulation to count the number of occurrences of the digit 7 in the given integer n, which is less than 79. It returns the if there are no such occurrences of 7.