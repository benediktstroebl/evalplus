```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return any(x > 0 for x in lst)

# Unit tests
test_max_element = lambda: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

test_max_element()

```
Do you want me to help you with anything else related to code?