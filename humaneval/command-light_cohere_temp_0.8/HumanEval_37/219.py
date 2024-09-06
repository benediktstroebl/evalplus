```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

# Test the function with a list of odd and even numbers
def test_sort_even():
    # Odd numbers
    odd = [1, 3, 5, 6]
    assert sort_even(odd) == [1, 3, 5, 6]
    # Even numbers
    even = [2, 4, 6, 8]
    assert sort_even(even) == [2, 4, 6, 8]
```