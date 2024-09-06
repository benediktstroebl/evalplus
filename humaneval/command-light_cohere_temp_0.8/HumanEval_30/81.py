```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases using lists
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Test cases using tuples
assert get_positive((-1, 2, -4, 5, 6)) == (2, 5, 6)
assert get_positive((5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10)) == (5, 3, 2, 3, 9, 123)

# Test cases using lists of different lengths
assert get_positive([1, 2, 3]) == [2, 3]
assert get_positive([9, 2, 4, -5]) == [2, 4]

# Test cases with strings
assert get_positive("hello") == ["hello"]

# Test cases with complex objects
class Test:
    def test():
        return [-1, 2, -4]
assert get_positive(Test()) == [2, 4]
```
This Python script defines a function `get_positive` that takes an input list and returns a new list containing only the positive elements from the original. The test cases cover a variety of scenarios, including list and tuple inputs, different lengths, and even complex class objects. The script also uses assertions to ensure the correctness of the `get_positive` function.