```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list is empty!")
    if len(lst) == 1:
        return lst[0]
    m = len(lst) // 2 + 1
    if m == len(lst) % 2:
        return (l[m - 1] + l[m]) / 2
    else:
        return l[m]

# Test suite
try:
    median([-10, 4, 6, 1000, 10, 20])
    print("Success!")
except ValueError as ve:
    print(f"Error: {ve}")
```