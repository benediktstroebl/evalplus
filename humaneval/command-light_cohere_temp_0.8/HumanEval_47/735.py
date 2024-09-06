```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
test_median = []
test_median.add([-10, 4, 6, 1000, 10, 20])
test_median.add([1, 2, 3, 4, 5])
test_median.add([1: 'median: True', 2: 'median: 3', 3: 'median: 6', 4: 'median: 10', 5: 'median: 15', 6: 'median: 15', 7: 'median: None', 8: 'median: None', 9: 'median: None')

# Run tests and display results
print('test_median:')
for test in test_median:
    print(f'Test: {test} - {test_median[test]}')
```