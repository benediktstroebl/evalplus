Here is a Python script with a self-contained function that solves the problem of sorting unique elements in a list:
```python
import pytest

def unique(lst):
    assert len(lst) == len(set(lst))
    assert all(set(lst)) == set()
    assert sorted(set(lst)) == sorted([int(x) for x in lst if x not in set(lst)])
    assert [x for x in lst if x not in set(lst)] == [x for x in lst]

# Run the tests using pytest
pytest.code.unique. This code Using ground Roman code that a way to run the tests for this function, using the pytest library.

Let's go over the code:
- `import pytest`: This line imports the pytest library, a popular Python testing framework.
- `def unique(lst):`: This defines a function named unique that takes a list lst as input and returns the sorted unique elements in that list.
- `assert len(lst) == len(set(lst))`: This statement checks that the length of the list lst is equal to the length of the set of its elements, using the set() function. This assertion will raise an AssertError if the lengths are not equal.
- `assert all(set(lst)) == set()`: This statement checks that the set() function returns the same set as the unique elements of the list, using the set() function to create a set from the list's elements. This assertion will raise an AssertError if the set is not equal to the empty set.
- `assert sorted(set(lst)) == sorted([int(x) for x in lst if x not in set(lst)])`: This statement checks that the sorted() function with a custom sorting function returns the same sorted set of unique elements in the list. This custom sorting function is a list comprehension over the unique elements in the list and checks if it is the same as the sorted set returned by the set() function.
- `assert [x for x in lst if x not in set(lst)] == [x for x in lst]:`: This statement checks that every element in the list lst is also in the unique set returned by the set() function. This assertion will raise an AssertError if any element in the list is not in the set of unique elements.

Note that this Python script defines a function that takes a list as input, sorts its unique elements, and then runs tests on the function to ensure its correctness.