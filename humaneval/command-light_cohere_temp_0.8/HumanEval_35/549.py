```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')  # Return negative infinity for empty list
    return max(lst)

def not_positive(lst):
    return any(x > 0 for x in lst)

# Test the max_element function
test_max_element = []
test_max_element.add([range(0, 4))
test_max_element.add([max_element(test_max_element))
test_max_element.add(max(test_max_element))
test_max_element.add(1, 2, 3)
test_max_element.add([min(test_max_element)+1, test_max_element)
test_max_element.add([max(test_max_element))

print(test_max_element)
```