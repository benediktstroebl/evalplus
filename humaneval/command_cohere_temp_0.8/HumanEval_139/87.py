```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    
    return factorial_list[n]

# Tests
def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 2450

test_special_factorial()
```

Make sure to have the necessary testing libraries installed, if not, you can do it with:
```bash
pip install pytest
```

The code defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It iteratively calculates the factorials of numbers from 2 to n and stores them in the `factorial_list`. Then, the value of `factorial_list[n]` is returned, which is the 'Brazilian factorial' for the given input `n`. 

The `test_special_factorial` function is a testing block that checks the correctness of the `special_factorial` function for different input values (0, 1, 2, 3, 4, and 5). 

Run the test block by calling `test_special_factorial()` and it will automatically verify the function's behavior against the predefined conditions.