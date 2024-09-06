```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. Finally, `sorted` is applied to organize the result. This approach ensures efficiency and clarity. The function can handle various cases and returns correct common elements. Test cases are valuable for ensuring accuracy; incorporate them into your code to verify function behavior.  Here is an example of how you might incorporate test cases:
```python
def test_common():
    # Test case 1
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case 2
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Add more test cases as needed
    # ...

test_common()
```

In this updated code, we encapsulate test cases within the `test_common()` function, which improves organization and allows for clear assertion statements. Each test case is asserted using the `assert` statement, which verifies that the actual output of the `common` function matches the expected output for each distinct scenario.  This method provides a structured framework for testing the `common` function effectively.  Feel free to add or modify test cases as needed to cover various scenarios.