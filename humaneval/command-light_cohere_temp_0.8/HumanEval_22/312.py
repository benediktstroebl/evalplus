```python
from typing import List
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

#Test cases
values_test = [1, 2, 3, 'three', ()):
    assert filter_integers(values_test) == [1, 2, 3]

string_test = ['three', 'four', 'five']
    assert filter_integers(string_test) == []

int_test = [1, 2, 3, 'four', 4]
    assert filter_integers(int_test) == [1, 2, 3]

dict_test = {'one': 1, 'two': 2, 'three': 'three'}
    assert filter_integers(dict_test) == []

list_test = [1, 2, 3, 'four', 4]
    assert filter_integers(list_test) == [1, 2, 3]
```  The function **`filter_integers`** accepts a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the value of the output for various input scenarios.