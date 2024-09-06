```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif len(lst) == 0:
        return float('-inf')
    else:
        return max(lst)

def not_positive(lst):
    return all(value > 0 for value in lst)

# Unit tests
test_max_element = [
    'List with all positive elements: [1, 2, 3]',
    'List with a single negative element: [-2]',
    'List with mixed positive and negative values: [-1, 2, -3, 4, -5]',
].map()

test_max_element.__ basements = [
    'Some error',
    None,
    float('-inf'),
].map()
```

I hope this self-contained Python script helps solve the problem of finding the maximum element in a list of numbers, and it includes unit tests.