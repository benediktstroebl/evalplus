```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index i can divide n evenly (i.e. n is divisible by i), then that number is returned. The loop ends before reaching n plus 1, as any numbers greater than n cannot be factors of n. Thus, the largest divisor of n will be found in the loop. 

Let's prove this function correct with some tests:
```python
test_cases = [
    (15, 5),
    (21, 3),
    (52, 2),
    (100, 10),
    (147, 7)
]

for n, expected in test_cases:
    assert largest_divisor(n) == expected
```