```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test
def test():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test 2
def test2():
    assert median([-20, -15, -10, -5, -3]) == -15

# Test 3
test3 = {'test': test2}

# Test 4
test4 = {'test': test}
``` 
This script defines a function median that calculates the median of a list of numbers, then provides several test cases to verify its correctness. It should produce the