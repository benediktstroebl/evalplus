Here's the solution:
```python
def fizz_buzz(n: int) -> int:
    d = {"7":[0,2,3]}
    return sum(1 for x in range(10) if x in d and n % 11**x == 0 or n % 13**x == 0)
```
This code defines a function fizz_buzz that counts the number of occurrences of the digit 7 in the range of integers less than n which are both divisible by 11 and 13. The function uses a list d to store the digits that appear in the numbers 7, 2, and 3, and uses a generator expression to iterate through the digits in the list while checking if each digit exists in the number being tested for and if n is divisible by 11 or 13 times that digit's power. The result is 1 for each digit that meets the criteria. 

Here are some tests that can be run to verify the correctness of the function:
```python
# Test 1: Verify function with n = 50
print(fizz_buzz(50)) == 0

# Test 2: Verify function with n = 78
print(fizz_buzz(78)) == 2

# Test 3: Verify function with n = 79
print(fizz_buzz(79)) == 3
```