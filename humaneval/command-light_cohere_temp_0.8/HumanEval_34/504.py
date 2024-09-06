```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test 1
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
# [0, 2, 3, 5, 9, 123]

# Test 2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unique(x)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test 3
class Test:
    def test(self):
        return unique([5, 3, 5, 2, 3, 3, 9, 0, 123])

test = Test()
result = test.result
print(result)
```