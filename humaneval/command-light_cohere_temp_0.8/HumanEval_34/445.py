```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

def test_unique():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(test_list)
    assert len(result) == 7
    assert set(result) == set([0, 2, 3, 5, 9, 123])

# Run the function and test it
unique(test_list)
test_unique()
```
This code defines a function `unique` that takes a list as an argument and returns a new list containing only the unique elements from the input list. It uses a method `seen` to keep track of elements that have been encountered, then iterates through the input list and appends elements to `result` if they are not in the `seen` set. The `test_unique` function contains a test list and asserts that the `unique` function produces the correct output for this input, ensuring the correctness of the function.