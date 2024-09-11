```markdown
### Prefix Generation Function

This script generates all possible prefixes of a given string, 
from the shortest to the longest.

#### Code

```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Parameters:
    string (str): Input string for which prefixes are generated
    Returns:
    List[str]: A list of prefixes in order from shortest to longest
    """
    prefixes = []
    for length in range(1, len(string) + 1):
        prefixes.append(string[:length])
    return sorted(prefixes, key=len)


# Example usage:
print(all_prefixes('abc'))
```

#### Output

```markdown
['a', 'ab', 'abc']
```

#### Explanation

This script works by generating prefixes of all possible lengths for the input string. It then sorts these prefixes by their length, resulting in a list of prefixes in order from shortest to longest.