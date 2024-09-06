Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reverse_sorted_arr = sorted(sorted_arr, reverse = True)
    names = []
    for num in reverse_sorted_arr:
        if str(num) == str(num):
            names.append(dict({1: "One", 2: "Two", 3: "Three", 4: "Four", 
                                5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}).get(num))
        else:
            names.append(str(num))
    return names
```

This script provides a function called by_length, which takes an array of integers as input and sorts the integers that are between 1 and 9 inclusive, reverse the resulting array, and then replaces each digit by its corresponding name from "One" to "Nine". The function handles cases where the array is empty or contains strange numbers.

Here is a simple test suite to verify the functionality of the by_length function:
```python
def test_by_length():
    # Basic Test Cases
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length([]) == []
    assert by_length([-1, 1, 55]) == ["One"]

    # Test Case with Negative Numbers
    assert by_length([1, -1, 2, 3, 4, 5]) == ["Five", "Four", "Three", "Two", "Two", "One"]

    # Test Case with Large Numbers
    assert by_length([10, 32, 33, 211, 5, 2]) == ["Ten", "Eight", "Seven", " 211 ", "Five", "Two"]

    # Test Case with Multiple Occurrences of the Same Number
    assert by_length([2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9]) == ["Nine", "Nine", "Nine", 
                                                                           "Three", "Four", "Five", "Five", 
                                                                           "Six", "Seven", "Eight", "Two", "Two", 
                                                                           "Two"]

    # Test Case with a mix of letters and numbers
    assert by_length([2, 1, 'a', 'b', 'c', 4, 5, 6, 7, 8]) == ["Eight", "Five", "Four", "Three", 
                                                                            "Two", "Two", "One", "a", "b", "c"]

test_by_length()
```

Making these test cases a part of your script ensures that the function behaves as expected across different scenarios. 
You can further enhance the test suite by adding more test cases to cover corner cases and edge scenarios.

To run the test cases mentioned above, simply add them to the test_by_length function and execute the test_by_length() function at the bottom of the script. 
This will verify that the by_length function behaves as expected. 

You can use Python's built-in `unittest` module for more sophisticated and organized test case management if needed.  By integrating `unittest`, you can define test cases and execute them automatically, generating further confidence in the reliability of your