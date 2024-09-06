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

def test_duplicate():
    assert unique([3, 3]) == [3]

if __name__ == "__main__":
    test_unique()
    test_duplicate()
 ```

I hope that the above code has a function unique that takes a list lst as input and returns a list containing the unique elements from that list. It uses a a set to keep track of elements that have been encountered, and it iterates through the input list and appends elements to result only if they are not present in the set. It then returns the the unique list.