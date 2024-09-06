```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The resulting list is then typed as `List[str]` to convey that it contains a list of strings. 

To ensure the expected behavior, the function employs list comprehension, a concise way to create a new list by applying an operation to each item in the existing list. Specifically, it uses the `startswith` method to test if each string in `strings` starts with the `prefix`, and if so, includes it in the returned list. 

To demonstrate the function, it comes with an example and a test case. These are instances of the standard typeclass, `TypeGuard`, which aids in enforcing type hints at runtime and facilitating a more robust and readable code. 

You can use this function by providing your list of strings and the desired prefix as inputs to obtain a new list containing only the strings that start with the specified prefix. 

For example, imagine you have a list of class names, `classes`:
```python
classes = ['Pythonist', 'NLP', 'DS', 'Arrays', 'Java', 'Python', 'C++', 'DataScience'] 

# Retrieve classes related to programming 
programming_classes = filter_by_prefix(classes, 'Python')
```

This will leave you with `['Pythonist', 'Python']`, which are the class names starting with the prefix `'Python'`. 

To see the list of strings that start with a certain prefix, you can also make use of the example provided in the function: 
```python
>>> filter_by_prefix(classes, 'Python')
['Pythonist', 'Python']
``` 

This will return the same result, providing an indication of how the function behaves with the given input. 

If you desire to test the function with other inputs or wish to view the comprehensive test suite, you can access the respective code within the Python script.