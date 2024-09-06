```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    got = max_element(test_list)
    assert got == expected, "Max element is not calculated correctly"

# Run the tests
test_max_element()
```
This Python script defines a function max_element that calculates the maximum element in a list. The function accepts a list as an argument and uses the built-in max() function to find the maximum element. The script also includes a test function that creates a test list and passes the max_element function to verify if it's correctly calculating the maximum element. The test function uses the test_list and compares the result of max_element against the expected maximum element (123 in this case). It also uses the assert statement to check if the actual maximum matches the expected maximum, failing if they don't match. 

Finally, the test_max_element function is called to run the tests.