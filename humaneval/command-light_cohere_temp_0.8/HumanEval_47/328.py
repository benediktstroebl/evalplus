```python
def median(l):
    """Return median of elements in the list l.
    if len(l) <= 1:
        return l[0]
    m = int(len(l) ** 0.5)
   
    if len(l) % 2 == 1:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]

# tests
def test_median():
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0

# main function
if __name__ == "__main__":
    test_median()
```