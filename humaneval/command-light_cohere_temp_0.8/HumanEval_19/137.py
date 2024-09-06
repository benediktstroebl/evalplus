```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    return ''.join(sorted(numbers, reverse=True))

# Test case 1
test_case1 = '''
    three one five
'''

# Test case 2
test_case2 = '''
    six three four
'''

# Test case 3
test_case3 = '''
    eight seven six
'''

# Test case 4
test_case4 = '''
    zero nine
'''

def test_cases() ->
    for test_case in [test_case1, test_case2, test_case3, test_case4]:
        assert sort_numbers(test_case) == 'zero nine'

test_cases()
```