```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This approach ensures that the function is optimized for efficiency and can handle various input scenarios while maintaining code conciseness. 

You can test the functionality using the provided test cases:
```python
def test_common():
    # Test cases
    test_cases = [
        ([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121], [1, 5, 653]),
        ([5, 3, 2, 8], [3, 2], [2, 3]),
        ([1, 2, 3], [3, 1, 2], [1, 2, 3]),
    ]

    for l1, l2, expected in test_cases:
        actual = common(l1, l2)
        assert actual == expected, f"Expected {expected}, but got {actual} for l1: {l1}, l2: {l2}"
```

The test cases cover a range of scenarios to ensure the function behaves as expected. 

The function's docstring provides insight into its purpose and behavior, including test cases that showcase its usage and expected output. This documentation helps other users better understand the function's purpose and how to apply it in their code.