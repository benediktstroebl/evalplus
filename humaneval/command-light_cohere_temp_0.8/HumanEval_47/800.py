```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return (len(lst) + 1) / 2
# Tests
for i in [median([3, 1, 2, 4, 5]) ,median([-10, 4, 6, 1000, 10, 20])]:
    print(i)
```