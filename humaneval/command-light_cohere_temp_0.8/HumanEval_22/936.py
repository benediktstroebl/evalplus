```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
values_test = [1, 2, 3, 'abc', {}, [0, 1, 2], [3, 'a', 4]]
assert filter_integers(values_test) == [1, 2, 3]

strings_test = ['a', 3.14, 5]
assert filter_integers(strings_test) == []

dict_test = {'a': 1, 'b': 2, 'c': 3}
assert filter_integers(dict_test) == []

list_of_lists_test = [[1, ['a'], [2, 3], ['d']]]
assert filter_integers(list_of_lists_test) == [1, ['a'], [2, 3]]

class_test = [1, None, [2, 3]]
assert filter_integers(class_test) == [1, 2, [2, 3]]
```