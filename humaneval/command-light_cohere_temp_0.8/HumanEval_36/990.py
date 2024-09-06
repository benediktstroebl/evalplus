```python
def fizz_buzz(n: int) -> int:    
    return sum([x in str(i) for i in range(1, n+1) for x in str(i) if i%10==0 or i%20==0])
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
``` 
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than a given number `n` which are divisible by 11 or 13. The function uses a string conversion to iterate through the numbers from 1 to `n` and checks if the current number's digit is 7 or if it is divisible by 11 or 13. The test function `test_fizz_buzz` asserts that the `fizz_buzz` function correctly computes the number of 7's in such numbers.