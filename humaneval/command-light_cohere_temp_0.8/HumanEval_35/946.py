```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test cases
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(my_list) == 123

my_dict = {'a': 5, 'b': 3, 'c': -5}
try:
    assert max_element(my_dict) == 5
except AssertionError as e:
    print(f"Error: {e}")

my_set = set([5, 3, -5])
assert max_element(my_set) == 5
```
The code defines a function max_element that takes a list as input and returns the maximum element in the list. It includes tests cases to test the function with different types of input.