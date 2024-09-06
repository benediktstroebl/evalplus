```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be set")
    if a == 0:
        return 0
    if b == 0:
        return 0
    
    # Counted loops and multiples test
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i
    
    # Largest integer not a divisor of a and b
    return max(a, b)

# Unit tests
test_greatest_common_divisor = []
test_greatest_common_divisor.append([5.list([5[int(0, 1), 2, 3, 4, 5), 6, 7, 8, 9, 10, 20, 25, 30, 35, 40, 45, 50, 60, 75, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 10000, 20000, 250000])
test_greatest_common_divisor.append([list([0, 1, 5, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 10000, 20000, 250000], [3, 5, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 100, 125, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 9000, 20000, 250000]])

def test_results():
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(10, 5) == 5
    assert greatest_common_divisor(200, 50) == 250
    assert greatest_common_divisor(3, 5) == 5
    assert greatest_common_divisor(0, 25) == 0
    assert greatest_common_divisor(10, 10) == 10
    assert greatest_common_divisor(9, 9) == 9
    assert greatest_common_divisor(9, 8) == 8
    assert greatest_common_divisor(10, 20) == 20
    assert greatest_common_divisor(20, 30) == 50
    assert greatest_common_divisor(35, 40) == 10
    assert greatest_common_divisor(40, 45) == 5
    assert greatest_common_divisor(20, 50) == 25
    assert greatest_common_divisor(250, 100) == 250
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(9, 70) == 50
    assert greatest_common_divisor(0, 100) == 0
    assert greatest_common_divisor(400, 50) == 250
test_results()
```
This Python script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It also includes a set of unit tests to ensure the correctness of the function. 

The greatest common divisor is the largest number that can evenly divide two numbers without leaving a remainder. It's calculated using a division by each number from 1 to