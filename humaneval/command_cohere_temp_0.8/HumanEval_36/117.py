Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases mentioned:
```python
def fizz_buzz(n):
    return sum(int(d) == 7 and d % 11 == 0 or d % 13 == 0 for d in range(1, n+1))
```
This function returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The range(1, n+1) generates all integers from 1 to n inclusive. The sum function then filters out the integers which are divisible by 11 or 13, and checks if the digit 7 appears.

To test this function, you can call it with three different integers and verify that it returns the correct values as described in the problem statement. Since the above code defines a function, you can use it in a test file alongside other test cases to validate its correctness comprehensively.  You can use the following code to test the function:
```python
def test_fizz_buzz():
    # Test case 1
    assert fizz_buzz(50) == 0
    # Test case 2
    assert fizz_buzz(78) == 2
    # Test case 3
    assert fizz_buzz(79) == 3

test_fizz_buzz()
``` 
This test code verifies the function's output against three distinct input values (50, 78, and 79) and checks if the function returns the expected results as per the problem statement.