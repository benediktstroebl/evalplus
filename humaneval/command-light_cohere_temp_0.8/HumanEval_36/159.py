```python
def fizz_buzz(n):
    count = 0
    for num in range(1, n+1):
        if all(c for c in str(num) if c == '7'):
            count += 1
    return count

# Test suite
test_fizz_buzz = [
    'fizz_buzz(50)', 0)
    'fizz_buzz(78)', 2)
    'fizz_buzz(79)', 3)
```
The function fizz_buzz calculates the number of occurrences of the digit 7 in numbers less than a given number n, then returns that count. It's designed using a simple loop and the all() function to check if all digits in num are '7'.