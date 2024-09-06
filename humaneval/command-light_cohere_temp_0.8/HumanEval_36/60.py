Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0:
        return 0
    
    if n % 10 == 7:
        return 1
    if n % 11 == 0 or n % 13 == 0:
        return 2
    
    return 0

# Test cases
test = unittest.py()

def test_fizz_buzz():
    """Test function fizz_buzz."""
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

if __name__ == "__main__":
    unittest.py().run()
```