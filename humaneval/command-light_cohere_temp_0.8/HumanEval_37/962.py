```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) % 2)

# Test the function with some examples
test_list = [5, 6, 3, 4]
assert sort_even(test_list) == [3, 6, 5, 4]

test_list = [1, 2, 3, 4, 5]
assert sort_even(test_list) == [1, 2, 3, 4]

test_list = [7, 8, 9]
assert sort_even(test_list) == [0, 7, 8, 9]
```
The function `sort_even` uses the key lambda function with a condition to sort even numbers in the list to the beginning and odd numbers to the end. It then returns the