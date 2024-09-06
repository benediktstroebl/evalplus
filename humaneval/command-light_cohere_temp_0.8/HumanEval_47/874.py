```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test cases
test_median = [
    [100, 200, 300, 400, 500],
    [-200, 400, 600, 800, 1000],
    [10, 20, 30, 40, 50],
    [1000, 2000, 3000, 4000, 5000],
]

for test_case in test_median:
    print(f"Testing median on {test_case}")
    assert median(test_case) == (test_case[len(test_case)//2] + test_case[len(test_case)//2])/2
```