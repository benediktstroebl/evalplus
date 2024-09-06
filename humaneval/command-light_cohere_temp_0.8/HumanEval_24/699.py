```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), 1)

def divisible(n: int, d: int) -> bool:
    return n % d == 0

# Test driver function
def test():
    assert largest_divisor(15) == 5

# Test case II
test_case2 = 10 

print("Case II divisible:", end, test_case2)
 assert largest_divisor(test_case2) == 5

# Test case III
test_case3 = 50000 

print("Case III divisible:", end, test_case3)
 assert largest_divisor(test_case3) == 50000 

# Test case IV
test_case4 = 30000
print("Case IV divisible:", end, test_case4)
 assert largest_divisor(test_case4) == 10000
``` 
This Python code defines a function `largest_divisor` that finds the largest divisor of a given number `n`. The `divisible` function checks if a number is divisible by a given divisor. The `test` function exercises the testing the `largest_divisor` function with various input values. The output will display the various test cases along with their expected results.