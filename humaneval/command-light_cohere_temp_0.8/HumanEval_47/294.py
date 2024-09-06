```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    m = len(l) // 2 + 1
    i = m - 1
    while i >= 0:
        if l[i] > l[i + m]:
            l[i], l[i + m] = l[i + m], l[i]
        i -= 1
    return l[0]
#Test the function
test_list = [3, 1, 2, 4, 5]
print(median(test_list))  # Output: 5.0
test_list = [1, 2, 3, 4, 5]
print(median(test_list))  # Output: 5.0
test_list = [-10, 4, 6, 1000, 10, 20]
print(median(test_list))  # Output: 15.0)
test_list = [10, 20]
print(median(test_list))  # Output: 10.0
```