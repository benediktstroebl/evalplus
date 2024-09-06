```python
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n+1):
        digit = int('0' + str(i % 10))
        if digit == 7 and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Test suite
test_fizz_buzz = []
test_fizz_buzz.push(78)
test_fizz_buzz.push(50)
test_fizz_buzz.push(79)
test_fizz_buzz.push(10)
test_fizz_buzz.push(27)
test_fizz_buzz.push(55)
test_fizz_buzz.push(72)
test_fizz_buzz.push(91)
test_fizz_buzz.push(88)
test_fizz_buzz.push(67)
test_fizz_buzz.push(73)
test_fizz_buzz.push(124)
test_fizz_buzz.push(69)
test_fizz_buzz.push(87)
test_fizz_buzz.push(91)
test_fizz_buzz.push(16)
test_fizz_buzz.push(111)
test_fizz_buzz.push(58)
test_fizz_buzz.push(85)
test_fizz_buzz.push(50)
test_fizz_buzz.push(63)
test_fizz_buzz.push(68)
test_fizz_buzz.push(66)
test_fizz_buzz.push(69)
test_fizz_buzz.push(114)
test_fizz_buzz.push(99)
```