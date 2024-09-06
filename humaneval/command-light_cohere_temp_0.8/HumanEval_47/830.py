```python
def median(lst):
    n = len(lst) // 2 + 1
    m = []
    for i in range(n):
        m.append(lst[i])
    m.sort()
    common(m)
    return m[n - 1]

def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 2, 1]
    assert median(lst) == 2.0  # True

# Example of the function
lst = [1, 2, 4, 5]
print(median(lst))  # Output: 2.0
test_median()
```