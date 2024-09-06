Here is a self-contained Python script that includes a function called **filter_by_prefix**, which is designed to solve the problem you have described:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function utilizes the **startswith** method to filter the input list of strings. It does so by checking whether each string in the list starts with the given **prefix**. 

To ensure the function behaves as expected with different inputs, it is then passed through a series of tests, which include an example with the function and test strings.