```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Example usage:
my_list = [5, 6, 3, 4]
print(sort_even(my_list))  # Expected output: [3, 6, 5, 4]
```
This Python function, sort_even, is designed to sort a list according to even numbers. It uses the _ `key` argument to the `sorted` function to sort the list. The `key` argument is a lambda function that returns the index of an element if it is even, and the index of the element plus one if the element is odd.