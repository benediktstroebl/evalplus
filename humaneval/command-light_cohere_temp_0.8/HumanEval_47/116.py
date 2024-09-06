```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 0:
        return (l[len(l)//2-1] + l[len(l)//2-2]) / 2
    else:
        return l[len(l)//2]

# Test cases
for _ in range(50):
    test_list = [random.randint(-1000, 1000) for i in range(len(test_list))]
    print("Test Case:", end="-)
    print(median(test_list))
    print("---")
```