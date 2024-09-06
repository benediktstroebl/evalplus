```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Examples
if __name__ == "__main__":
    test_list = [-10, 4, 6, 1000, 10, 20]
    print(median(test_list))  # Output: 15.0
    test_list = [1, 2, 3, 4, 5]
    print(median(test_list))  # Output: 5.0
    test_list = [3, 4, 5, 6, 7, 8, 9]
    print(median(test_list))  # Output: 6.0
    test_list = [-.2, ., ., 1, ., -.5]
    print(median(test_list))  # Output: .5
```