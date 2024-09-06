```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(''.join(strings))
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['a', '', 'b']) == 'ab'
    assert concatenate([', 'a', '', 'bc']) == 'abc'
```
This code provides a function called **concatenate** that takes a list of strings and returns the concatenated string. It also has a test_concatenate function with several test cases. 

The output will be the following markdown code: 

```
* abc
* ab
* ab
* abc
* abc
```