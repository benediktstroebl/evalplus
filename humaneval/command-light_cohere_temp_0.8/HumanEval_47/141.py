```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function with a list with odd and even length
test_list = [-10, 4, 6, 1000, 10, 20]
assert median(test_list) == 15
test_list2 = [1, 2, 4, 5, 6, 10, 20]
assert median(test_list2) == 5

# Test the function with a list of numbers
test_numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10]
assert median(test_numbers) == 7
```