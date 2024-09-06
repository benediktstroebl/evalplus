```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. 

The concise nature of this approach makes it readable and expressive, but it also may be more challenging to comprehend for those who are newer to Python or functional programming concepts. If you were to provide this code to a classroom of students learning Python, it may be beneficial to provide the more verbose version you had previously provided to help students understand the concept more effectively. 

This function is reusable and efficiently solves the stated problem, as demonstrated by the following example:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```