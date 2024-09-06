```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2) - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test the function with various input lists
for i in [median([3, 1, 2, 4, 5]) , median([-10, 4, 6, 1000, 10, 20]) ,median([1, 2, 3, 'abc' ,4])]:
    print(i)
```