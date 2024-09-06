```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest. """
    
    # Initialize a result list
    factors = []
    
    # Loop through all numbers from 2 to the square root of the input number
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n)//i)
            n = n // i
        
    return factors

# Test the function
def test_factorize():
    n = 25
    result = factorize(n)
    print(result)
    assert len(result) == 5
    assert result[0] == 5

# Test again
test_factorize()
```