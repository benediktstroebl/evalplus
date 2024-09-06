```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test the function with different inputs
values_list = [['a', 3.14, 5, 1, 2, 'abc', {}, []]
print(filter_integers(values_list))  # Expected output: [1, 2, 3, 5]

values_dict = {1: 'a', 3: 3.14, 5: 5, 'abc': 'abc', None: None}
print(filter_integers(values_dict))  # Expected output: [1, 3, 3. same

values_string = "a3" + "5"
print(filter_integers(values_string))  # Expected output: []
```