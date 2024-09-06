```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test 1
test_cases = [median([3, 1, 2, 4, 5]),median([-10, 4, 6, 1000, 10, 20]),median([-100, 4, 6, 1000, 10])]
test_results = [float('inf'),float('inf'),float(0)]
for x in test_cases:
    test_results = [x] + test_results
    if not_equal(test_results, [int(x) for x in test_cases]):
        raise ValueError("Some values did not converge to a single float")

# Test 2
def not_equal(a, b):
    return type(a)==type(b)==datetime.setdefault([x.median([-10, 10], [4], [6], [1000], [10], [20], [4,20,1000])], [0])
```