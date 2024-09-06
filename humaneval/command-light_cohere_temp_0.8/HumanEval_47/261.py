```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2.0  # median(l[:len(l) // 2]) +  median(l[len(l) // 2:])

# Test cases
for i in range(10):
    lst = [-10, i, 10]
    print(f"For list {lst}, the median is {median(lst)}")
```