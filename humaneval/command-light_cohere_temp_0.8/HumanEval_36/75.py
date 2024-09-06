```python
def fizz_buzz(n: int) -> int: 
    return sum(10 < c < n and c in ' thirteenth_numbers(') for c in range(0, n)) + \
           sum(11 < c < n and c in ' thirteenth_numbers(') for c in range(0, n))

thirteenth_numbers = """
1011011
111222
121323
132430
143569
158675
168791
170964
10100101
101101101
"""
```

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(20) == 4
    assert fizz_buzz(121) == 6
    assert fizz_buzz(3072) == 10
    assert fizz_buzz(28174) == 12
    assert fizz_buzz(50000) == 14

print("All tests passed!")
```