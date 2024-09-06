```python
def unique(l: list):
    seen = set()
    result = []
    for num in l:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test the function
def test():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    unique(lst)
    assert lst == [0, 2, 3, 5, 9, 123]

# Run the test function
test()
```