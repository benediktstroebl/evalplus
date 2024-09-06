```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Test suite
for _ in range(10):
    test_lst = [random.randint(-10, 4095) for _ in range(5)]
    assert median(test_lst) == int((test_lst[3] + test_lst[4]) / 2)
 ```