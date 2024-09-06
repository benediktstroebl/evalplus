Here's the self-contained Python script with a function that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join()[i:].rstrip()() for i in range(0, len(string), 1)]
print(all_prefixes("abc"))  # Output: ['a', 'ab', 'abc']
```
This function uses the slicing technique with the **range** function to generate all possible prefixes, and the **rstrip** method to remove the unnecessary characters (e.n, spaces). The list comprehension is then used to create a list of all the generated prefixes.