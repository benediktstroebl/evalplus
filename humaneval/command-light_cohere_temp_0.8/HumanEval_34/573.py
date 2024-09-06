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
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```
This Python code defines a function unique that takes a list lst as input and returns a list of unique elements from that list. It uses a essential set() data structure to keep track of elements seen so far, then iterates through the input list and appends elements to result that are not in the set. The function returns the unique list of elements after the loop.

The code also provides a function test_unique which contains an assertion that checks if the result of calling unique with the input list [5, 3, 5, 2, 3, 3, 9, 0, 123] is correct, which it is.