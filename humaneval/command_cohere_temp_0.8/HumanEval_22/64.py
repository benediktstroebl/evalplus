```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type as input. It uses a list comprehension to iterate through each element in the input list. If the element is an instance of the int type, it means it's an integer, and it gets included in the `result` list. Finally, the function returns the `result` list containing only the integer values from the original input list, regardless of other data types. 

To use the script, just run it, and it will output the list with integers. 

```python
filter_integers(['a', 3.14, 5])
```
```
[5]
```

```python
filter_integers([1, 2, 3, 'abc', {}, []])
```
```
[1, 2, 3]
``` 

If you want to test the function using specific test cases, you can add the corresponding test blocks to verify the function behavior against different inputs.