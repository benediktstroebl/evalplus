```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

#Test the function with a sample list
# Make sure to adjust the list with your own data!
print(median([-10, 4, 6, 1000, 10, 20] ))
```