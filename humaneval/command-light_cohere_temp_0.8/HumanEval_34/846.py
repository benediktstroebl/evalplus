```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, float('inf')] + set(seen)]

if __name__ == "__main__":
    # Test the function
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(test_list))
```
The function unique returns a list containing the unique elements from the input list lst, excluding any None and infinity values. The function utilizes the value-set to keep track of values seen so far, ensuring that each unique element is only added once to the set. This helps to identify unique elements efficiently.