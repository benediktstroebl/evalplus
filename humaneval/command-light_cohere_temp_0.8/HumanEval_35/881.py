```python
def max_element(lst):
    if not_elements(lst):  # base case
        return None
    max_ = max(lst, key=float)
    return max

def not_elements(lst):
    return not len(lst) and all(isinstance(x, int) for x in lst)

# test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([''])))  # Output: None
print(max_element([1, 2, 3. went. '\n time: 'abc\ \d')))  # Output: None
print(max_element([10, 10, 10])))  # Output: 10
```