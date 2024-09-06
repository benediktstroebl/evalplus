```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements from l. Inside the function, a set seen is used to keep track of already-seen elements. The function then iterates over the input list, checking if each element is already in the seen set. If the element is not in the set, it is added to the set using the method not seen.add(element), and then added to the unique result list. The element is not added to the result if it was already present in the set, ensuring that only unique elements are included in the final output. The function returns a sorted list of these unique elements.

Here is an example of how to use this function:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

This will return a list of the unique elements in the input list, in this case, [0, 2, 3, 5, 9, 123].

The code includes a docstring at the beginning to provide a clear description of the function's purpose, making it easier for developers to understand its functionality and expected inputs/outputs. 

This approach provides a straightforward and efficient solution to the problem of finding the sorted unique elements within a list. 
	
	Feel free to ask any questions or for further assistance on the problem as needed!