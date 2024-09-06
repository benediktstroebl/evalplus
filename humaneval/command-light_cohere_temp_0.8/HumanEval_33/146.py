```python
def sort_third(lst):
    """This function sorts a list so that values divisible by three appear in their correct positions, and the rest of the values are sorted normally."""
    lst = list(map(lambda x: x if x % 3 == 0 else x + 1, lst))
    return sorted(lst)

# Test the function with sample inputs
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
assert result == [2, 6, 3, 4, 8, 9, 5]

# Another test with list of strings
test_str_list = ["python", "JavaScript", "C++", "SQL"]
result = sort_third(test_str_list)
assert result == ["C++", "SQL", "python", "JavaScript", "2", "6", "8"]
```
The above script defines a function `sort_third` which sorts the input list so that the values divisible by 3 appear in their correct positions. The map function uses a value of each element of the list and if it is divisible by 3, then we add 1 to it. If it's not divisible by 3, then we leave the value as it. The `test_list` and `test_str_list` are then passed to the `sort_third` function and the results are checked using the `assert` statement to verify if the output of the function matches the expected output.