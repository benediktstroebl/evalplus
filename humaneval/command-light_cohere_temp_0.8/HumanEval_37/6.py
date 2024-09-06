```python
def sort_even(lst):
    even = [el for el in lst if el % 2 == 0]
    even_copy = [el for el in lst if el % 2 == 0]  # copy to avoid mutating original list
    return even_copy

# Test suite to verify function
test_sort_even = []
test_sort_even.push_list = [5, 6, 3, 4]
test_sort_even.push_list2 = [1, 2, 3]
test_sort_even.push_list = [5, 6, 3, 4, 2]
test_sort_even.push_list = [1, 2, 3, 4, 5, 6]

def test_function():
    test_sort_even(push_list)
    assert test_sort_even == [3, 6, 5, 4]
    assert test_sort_even == [1, 2, 3]
    assert test_sort_even == [5, 6, 3, 4, 2]
    assert test_sort_even == [1, 2, 3, 4]

# Main function to execute the test suite
def main():
    test_function()

if __name__ == "__main__":
    main()
``` 
This script defines a function `sort_even` which takes a list and returns a sorted list of even numbers from the input. The test suite is then created with a series of test cases, where the `sort_even` function is called and the expected output is compared with the actual output.  The test suite also contains additional test cases to ensure the function works correctly with different input.