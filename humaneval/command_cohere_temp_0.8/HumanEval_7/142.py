```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. This function utilizes list comprehension, and the `in` operator to solve the problem. It iterates through each string in the input list and checks if the `substring` is present in each string. If it is, the string is included in the output list. If the `substring` is not found in the list, that element is not included in the output.  This approach ensures that the function is efficient, scalable, and easy to understand.  By applying the `in` operator, we can swiftly filter out strings that contain the substring without the need for additional logic.  This simplistic approach is elegant and efficient in its functionality, demonstrating the power and utility of Python's built-in list comprehension and `in` operator.