```python
def max_element(lst):
    if not_elements(lst):
        return None  # Handle empty list
    return max(lst)

def not_elements(lst):
    return all(lst) and len(lst) > 0

# Unit tests
test_max_element = [
    assert max_element([1, 2, 3]) == 3, "Return 3 for [1, 2, 3]"
])

test_valid_input = [
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123, "Return 123 for valid input"
]

if __name__ == "__main__":
    test_max_element. When executed, this script will run all the unit tests and demonstrate the functionality of the max_element function.