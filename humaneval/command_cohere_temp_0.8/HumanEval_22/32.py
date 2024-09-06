```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = [item for item in values if isinstance(item, int)]
    return integers
```

The function calls itself `filter_integers` and takes a list of values of any type as an argument. It uses a list comprehension to iterate over each item in the input list and checks if the item is an instance of the `int` class using the `isinstance()` function. If the item is an integer, it is included in the `integers` list, and finally, this list is returned. 

To run the code, you need to save it in a Python file (e.g., `filter_integers.py`) and execute it using the Python interpreter:
```bash
python filter_integers.py
``` 

If the script is executed successfully, there will be no output, and the returned list of integers will be printed only if there are any integers in the list. You can also import and use the function in another Python file. 

The script comfortably passes the test cases provided earlier:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```