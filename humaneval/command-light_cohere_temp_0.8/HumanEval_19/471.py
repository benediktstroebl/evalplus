```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string containing numbers from zero to nine."""
    return "".joingrep(str.split(" ")[::(len(str.split(" ")) -1:2])
            .map(str.ch strings)
            sorted(
                    key=lambda x: int(x) - int('zero'),
                    reverse=True)

# Test case 1
test_sort_numbers_valid = """
>>> sort_numbers('three one five')
'one three five'
"""

# Test case 2
test_sort_numbers_invalid = """
>>> sort_numbers('one three five')
"""

# Test case 3
test_sort_numbers_empty = """
>>> sort_numbers('')
""")

# Test case 4
test_sort_numbers_duplicates = """
>>> sort_numbers('two three four five six seven eight nine')
"""

# Test case 5
test_sort_numbers_wrong_delimit = """
>>> sort_numbers('   one two three four five six seven eight nine')
"""

def test_main():
    assert test_sort_numbers_valid == 'one three five'
    assert test_sort_numbers_invalid == 'zero nine'
    assert test_sort_numbers_empty == ''
    assert test_sort_numbers_duplicates == 'six seven eight nine'
    assert test_sort_numbers_wrong_delimit == 'two four six eight nine'
    print("All tests passed!")
test_main()
```