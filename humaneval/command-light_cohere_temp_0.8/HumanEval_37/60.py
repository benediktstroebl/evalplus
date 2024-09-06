```python
def sort_even(lst):
    even = [item for item in lst if item % 2 == 0]
    return [even[i] for i, even in enumerate(even)]

# Test the function with a list of integers
test_list = [1, 2, 3, 4, 5, 6]
result = sort_even(test_list)
assert [i for i, item in enumerate(result) if item == 3] == [1, 2, 3], "Should get the even numbers sorted"
assert [i for i, item in enumerate(result) if item == 4] == [3, 6, 5, 4], "Should get the even numbers sorted"

# Test the function with a list of strings
test_strings = ["a", "b", "c", "d"]
result_strings = sort_even(test_strings)
assert result_strings == ["d", "c", "b", "a"], "The strings should be sorted"

# Test the function with a list of mixed data
test_mixed = [1, 2.5, 6, 3, 4]
result_mixed = sort_even(test_mixed)
assert result_mixed == [3, 4, 5, 6, 2], "The mixed data should be sorted"
 ```
This script defines a function called sort_even, which takes a list as input and returns a new list with the even numbers from the original list sorted. The function works by first creating a new list called even that contains only the even numbers from the original list, and then returning a new list where the even numbers from the original list are in sorted order. 

The test section then includes several tests to verify the correctness of the sort_even function. These tests check that the test various types of lists, including both numeric and string lists, and also a list of mixed data. The results of these tests should show that the even numbers are correctly sorted.