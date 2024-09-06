```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    elif len(lst) % 2 == 0:
        return (lst[len // 2 - 1] + lst[len // 2]) / 2
    else:
        return lst[len // 2]

# Test the function
for i in range(0, 21):
    print(median([i, i+1, i*3]))  # Test even length
    print(median([1, 2, 3, 4, 5, 6]))  # Test odd length
```