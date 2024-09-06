```python
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n+1):
        if int(str(i))[1:] == 7 or i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Test case: Check if the function correctly counts occurrences of 7 in numbers less than n which are divisible by 11 or 13

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(25) == 4
assert fizz_buzz(81) == 0

# Test script
test_fizz_buzz()

``` 
This code defines a function `fizz_buzz` that calculates the number of occurrences of the number 7 in a series of numbers that are either divisible by 11 or 13. The `test_fizz_buzz` function contains assertions that verify the correctness of the `fizz_buzz` function with different input values.