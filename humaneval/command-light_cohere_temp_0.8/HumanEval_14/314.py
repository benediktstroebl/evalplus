```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x != '']
test_data = {
    'abc': ['a', 'ab', 'abc'],
    'hello world': ['hello', 'world'],
    ''': [],
    'ape ---------': ['ape'],
    'a': ['a'],
    '': []
}
test_case_results = {
    test_data[key]: test_prefixes(test_data[key]) for test_prefixes in test_data.
}
print(test_case_results)
``` 
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest using a list comprehension. The test_data dictionary contains a variety of test cases with input strings and expected prefix lists. The script_case_results dictionary is created by applying the all_prefixes function to each test case, and then printing the results.