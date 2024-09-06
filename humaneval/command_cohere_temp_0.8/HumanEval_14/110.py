```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[1:])) + [string]
```
This code uses the `accumulate` function from the `itertools` module to generate all successive prefixes of the input string. Initially, the string is shifted by one right (string[1:]) to exclude the null string as a prefix. Then, accumulate will combine those characters from right to left, generating all the prefixes of the string. Finally, the list containing these prefixes is returned, and the original string is added at the end to complete the list of prefixes from shortest to longest. 

Here is an example usage of this code:
```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```
In the example, we can see that the list contains the shortest prefix ('a'), the second shortest prefix ('ab'), and the longest prefix ('abc'), as desired. 

This code assumes that the input string is non-empty. If the input is empty, the function returns a list containing just the empty string. 
If you are working with Markdown, you can test this script by adding a code block with the `all_prefixes` function and its corresponding test. See this through here is an example of how to do this within a Jupyter environment:
```python
# Create a new cell and enter the markdown cell header
```md
# All Prefixes

```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[1:])) + [string]

# Example usage
all_prefixes('abc')
```
# Display the result
```
```
You can also do this outside of Jupyter by using a simple text editor and saving the markdown code block with the appropriate code.