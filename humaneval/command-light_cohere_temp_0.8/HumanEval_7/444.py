```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The code implements a function called **`filter_by_substring`** that filters an input list of strings to only include those that contain a given substring. This is function utilizes the specific to the input **`List[str]`**` and **`substring`** to filter out the desired elements. 

The function utilizes the **`find`** method from the string object to determine if each element of the input string contains the given substring. 

This function is self-contained and provides a clear and concise way to solve the problem.