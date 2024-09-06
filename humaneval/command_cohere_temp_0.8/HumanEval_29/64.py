```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that begin with the `prefix`. It uses a list comprehension, which is a concise way of expressing a for loop in Python. 

To see how this function works, let's break it down with an example in which we have a list of fruits and we want to filter those fruits that are healthy, in this case, starting with the prefix "healthy".
```python
fruits = ['healthy apple', 'healthy banana', 'orange', 'kale smoothie', 'healthy peach']
prefix = 'healthy'

filter_by_prefix(fruits, prefix)
```

The output will be:
```python
['healthy apple', 'healthy banana', 'healthy peach']
```

In this example, the list `fruits` contains strings that have fruits and some of them are healthy. The function `filter_by_prefix` takes the list of fruits and the prefix "healthy" as input and returns only the fruits that start with the given healthy prefix.