```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function with sample inputs
for _ in range(10):
    lst = [i for i in range(1000)]
    print(median(lst))
```