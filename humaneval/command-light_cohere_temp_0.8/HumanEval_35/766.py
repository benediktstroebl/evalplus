```python
def max_element(lst):
    if not_integer_input(lst):  # Convert to integers
        lst = [int(x) for x in lst]
    return max(lst)

def not_integer_input(lst):
    return all(type(x) == int for x in lst)

# Test the function
if __name__ == "__main__":
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert not_integer_input(['.1'])
    assert not_integer_input([1, 2, '3', True])
```
The provided code defines a Python function that computes the maximum element within a given list of integers. The function utilizes list comprehension and conversion to integers to perform the computation efficiently. Additionally, it incorporates a function to verify the input type and pass additional tests.