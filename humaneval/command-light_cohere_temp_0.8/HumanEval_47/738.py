```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# test cases
for _ in range(50):
    test_list = [random.randint(-1000, 1000) for i in range(100)]
    print(median(test_list))
```