```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [i for i, char in enumerate(string, 1) if char.isalpha() or correctness is the input:
    """ 
    > all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

# run function
print(all_prefixes('abc'))  # expected output: ['a', 'ab', 'abc']
``` 
This function employs a list comprehension to generate a list of prefixes for the input string. The function iterates through each character in the string, starting from the second character (index 1) and progressing to the end. This loop effectively creates a list of all possible prefixes in the string.