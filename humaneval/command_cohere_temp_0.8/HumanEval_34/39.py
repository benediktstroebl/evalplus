```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This Python script defines a function unique that takes a list `l` as an argument and returns a sorted list of its unique elements. It achieves this by employing a set `seen` to keep track of the encountered elements in the input list `l`. Subsequently, it utilizes a list comprehension to iterate through each element in `l`, checking if it has already been marked as seen. If an element hasn't been marked seen, it adds it to the set using `seen.add(element)` and includes it in the final result. The output is a list of unique elements that have been sorted in ascending order.

The script satisfies the given problem statement and corresponds to the provided tests, as it correctly returns the unique elements from the input list in a sorted order.

This optimized approach uses the set data structure to efficiently track unique elements and the list comprehension to traverse the input list, resulting in a concise and effective solution.