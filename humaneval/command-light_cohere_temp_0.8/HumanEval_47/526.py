```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    return (len(lst) + 1) / 2 * (lst[(len(lst) + 1) / 2] + lst[len / 2])

# Test the function
for i in range(0, 10):
    test_list = [i, i*2, i+3, i*i]
    print(median(test_list), end=' ')
```