Here's a self-contained Python script that provides a function to filter an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains() method from the string module to check if each string in the input list contains the given substring. The output is a list of all strings that contain the substring.

Let's breakdown the code:
1. Function declaration: It takes two parameters: a List[str] (which can be of any string type) and a substring (str) that we are searching for.
2. Initializer: A list of strings and a substring is passed as arguments to the function.
3. Filter logic: It uses the list comprehension to iterate over each string in the input list. For each string, it uses the contains() method from the string module to check if the string contains the given substring.
4. The containing condition: it checks if the string contains the given substring by using the contains() method. If the condition is true, it adds the string to the result list.

5. Return value: Finally the function returns a list of all the strings from the input list that contain the given substring.

This function is self-contained, and it efficiently filters the strings from the input list for ones that contain the specified substring.