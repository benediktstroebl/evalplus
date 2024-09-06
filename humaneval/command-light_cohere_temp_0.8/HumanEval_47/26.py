```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test
def test():
    lst = [-10, 4, 6, 1000, 10, 20]
    print("Median:", median(lst))

if __name__ == "__main__":
    test()
```