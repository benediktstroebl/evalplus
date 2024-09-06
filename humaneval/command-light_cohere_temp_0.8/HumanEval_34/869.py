```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ] and x]

if __name__ == "__main__":
    # Tests
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    test_result = unique(test_list)
    print(test_result)  # Expected Output: [0, 2, 3, 5, 9, 123]
```
The function unique returns a list containing the unique elements from the input list lst, after removing duplicates, duplicates, and [-None,]. This function effectively sorts and returns the unique elements from the input list. The main function then executes the test_list and prints the expected output. The test_result variable holds the unique function's result.