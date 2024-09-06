```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
# Test cases
median([-10, 4, 6, 1000, 10, 20])
# Correct answer: 15.0
median([1, 2, 3, 4, 5])
# Correct answer: 5.0
median([-20, -10, -5, -3, -1])
# Correct answer: 2.0
median([3, 1, 2, 4, 5])
# Correct answer: 5.0
median([10, -20, -40, -100])
# Correct answer: -20.0
median([1, -10, -1, -20, -40])
# Correct answer: -1.0
```