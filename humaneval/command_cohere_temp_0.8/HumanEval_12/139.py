```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, loops through the list to determine if there is a single unique string, and returns that string if there is only one unique value and returns the longest string if there are more than one unique values but and returns None if the list is empty. 

Here is an example when you use the longest function to parse through a list of strings and return the longest string:
```python
longest(['a', 'bb', 'ccc']) # 'ccc'
```

Here is another example when you use the longest function to parse through a list of strings and return the first string in case of multiple strings of the same length:
```python
longest(['a', 'b', 'c']) # 'a'
```

And here is the last example when the function returns None in an empty list:
```python
longest([])
```

The function can also be tested with markdown code blocks provided in the original prompt and should return the following outputs:
```
```python
longest([])
None

longest(['a', 'b', 'c'])
'a'

longest(['a', 'bb', 'ccc'])
'ddd'
```

The way this function works is that it first checks if the list is empty or not and returns None immediately if it is empty. Then, it checks the uniqueness of strings using the set which is much faster and has a `O(1)` time complexity for checks like this, and if there is a single string or more than one string but they have the same length, it just picks the first one as there is no uniqueness anyway. Finally, in the case of multiple strings with distinct lengths, it uses the `max` function with the `key` argument to pick the longest one.  This approach has a `O(n)` time complexity in the worst case where `n` is the number of elements in the list.  This is an efficient and effective solution to the problem.