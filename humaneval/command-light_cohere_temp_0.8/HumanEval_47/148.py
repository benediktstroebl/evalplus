```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test suite for the function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([3, 4, 5, 6, 7]) == 5.0
    assert median([10, 20, 30, 40, 50]) == 30.0
def main():
    test_median()

if __name__ == "__main__":
    main()
```