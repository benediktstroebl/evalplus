```python
def fizz_buzz(n: int) -> int: 
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0 
    for num in range(1, n+1):
        d = str(num)
        if(len(d)==1 and d=='7' or d=='11' or d=='13'):
            count += 1 
    return count
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```