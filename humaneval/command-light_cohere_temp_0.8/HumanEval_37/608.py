```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) % 2)

# Example function test
def test(test_list):
    assert sorted(test_list) == [3, 6, 5, 4]

# Example usage
test_list = [5, 6, 3, 4]
test_result = sort_even(test_list)
print("Test Result:", test_result)
```