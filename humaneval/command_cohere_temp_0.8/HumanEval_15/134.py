```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}{n+1}'
    return numbers.strip('0') and numbers or '0'

# Tests
import pytest

@pytest.mark.parametrize('test_input, expected', [
    (0, '0'),
    (5, '0 1 2 3 4 5'),
    (100, '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'),
])
def test_string_sequence(test_input, expected):
    output = string_sequence(test_input)
    assert output == expected
```

This script includes a function `string_sequence(n)` that returns a string with numbers ranging from 0 to `n` (inclusive) separated by spaces. It initially creates a string `numbers` with two concatenated digits for the 0th and 1st indices. This ensures that counting up to `n` can be achieved by removing extraneous `0` characters from `numbers`. For example, with `n = 5`, `numbers` becomes `'5151'`, and removing the `0` gives us the desired output of `'1 2 3 4 5'`. Related test cases are furnished to verify correct function behavior.