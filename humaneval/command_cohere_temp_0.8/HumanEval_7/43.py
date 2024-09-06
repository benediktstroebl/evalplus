```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, accompanied by an informative docstring that describes the purpose and behavior of the function and provides example usage. 

To use this function, you can import it into your workspace and call it with an input list of strings and a substring as follows:
```python
import filter_by_substring

result_list = filter_by_substring.filter_by_substring(input_list, "substring")
``` 
It's important to note that the function assumes the substring is a valid input and will yield the fastest results for straight substring searches without additional complexity. If you're working with large datasets or needing more sophisticated searching, additional optimizations or approaches may be necessary.