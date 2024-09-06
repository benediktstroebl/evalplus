```python
def median(l: list):
    n = len(l)
    m = n // 2
    if n % 2 == 1:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Test case 1
test_cases = [
    [-10, 4, 6, 1000, 10, 20],
    [3, 2, 4, 5],
    [0, 5, 6, 7, 8, 9, 10],
    [1000, 2000, 3000, 4000, 5000, 6000, 7000]
]

for test_case in test_cases:
    print(median(test_case))  # Output should be the median value of the list
```