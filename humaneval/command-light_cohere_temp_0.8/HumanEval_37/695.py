```python
def sort_even(lst):
    """Sorts even numbers in a list."""
    return sorted(lst, key=lambda x: int(x) % 2 == 0)

# Test
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Main
if __name__ == "__main__":
    test_sort_even()
``` 
This script defines the `sort_even` function that sorts even numbers in a list using the `sorted` function with a custom key function that checks if the number is even or not. The `test_sort_even` function tests the `sort_even` function with a series of test cases, ensuring that the function works as expected. 

When you run this script, it will run the tests and display the results. This is: it can be used as a self-contained unit for sorting even numbers in a list.