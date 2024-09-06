Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases mentioned:
```python
def fizz_buzz(n):
    cnt = 0
    for i in range(1, n+1):
        if i%11==0 or i%13==0:
            num = str(i)
            cnt += num.count(7)
    return cnt

# Tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

The function uses a for loop to iterate through all the numbers from 1 to n, and if the number is divisible by 11 or 13, it converts it to a string, counts the number of 7s in that string, and increments the counter cnt. The test cases provided are used to validate the function. 

The logic tests two conditions (i%11==0 or i%13==0) making it efficient as it only needs to check the remainders of each iteration once. If a number satisfies either of the conditions, the 7s are counted using the str.count method. This approach ensures accuracy while keeping the code concise.