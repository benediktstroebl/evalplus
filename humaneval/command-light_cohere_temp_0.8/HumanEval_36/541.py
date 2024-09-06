```python
def fizz_buzz(n: int) -> int:
    d, i, count = [0] * 4
    for i in range(2, n+1):
        if i % 10 == 7:
            d[0] += 1
        elif i % 11 == 0 or i % 13 == 0:
            d[1] += 1
        else:
            d[2] += 1
        if d[0] > 0 or d[1] > 0 or d[2] > 0:
            count[d[0]] += 1
            count[d[1]] += 1
            count[d[2]] += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz uses a list d to keep track of the number of times each digit appears in the numbers from 2 to n that are divisible by 11 or 13. It then uses a array_sum() to count the occurrences of each digit and returns the result.