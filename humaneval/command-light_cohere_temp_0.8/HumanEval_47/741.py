```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2] + l[n//2-1]) / 2
    else:
        return l[n//2]

# test suite
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# main program
if __name__ == "__main__":
    lst = [-10, 4, 6, 1000, 10, 20]
    test_median()
```