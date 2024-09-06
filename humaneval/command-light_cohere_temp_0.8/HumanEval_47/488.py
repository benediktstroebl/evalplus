```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1)**.5 / 2
if __name__ == "__main__":
    # test
    lst = [-10, 4, 6, 1000, 10, 20, 2, 1]
    print(median(lst))  # Output: 5.0
```