```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and x not in [-None, -])]

unique([5, 3, 5, 2, 3, 3, 9, 0, 123])  # [0, 2, 3, 5, 9, 123]

# Test the function with a string
test_str = "unique text"
test_list = [test_str, "Hello", "test"]
test_result = unique(test_list)
print(test_result)
```