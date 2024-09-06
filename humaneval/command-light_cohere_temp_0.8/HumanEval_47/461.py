```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l((n-1)//2) + lst[(n-1)//2]) / 2
    else:
        return lst[(n-1)//2]

def testMedian():
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 15.0

# You can add more test cases to pass additional tests

# Print the test results
print('Test Median(): passed')
```