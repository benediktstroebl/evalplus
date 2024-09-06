```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers. Test cases pass!oo
    test:
    print(sort_numbers('three one five'))
    assert sort_numbers('three one five') == 'one three five'

    print(sort_numbers('6 four 5'))
    assert sort_numbers('6 four 5') == 'six four five'

    print(sort_numbers('Zero One Two Three'))
    assert sort_numbers('Zero One Two Three') == 'zero one two three'

    print(sort_numbers('9 eight seven'))
    assert sort_numbers('9 eight seven') == 'nine eight seven'

    print(sort_numbers(' Nine Eight Seven'))
    assert sort_numbers(' Nine Eight Seven') == 'nine eight seven'

    print(sort_numbers('10 nine 8'))
    assert sort_numbers('10 nine 8') == 'ten nine eight'

    print(sort_numbers('deadbeefghijkl'))
    assert sort_numbers('deadbeefghijkl') == 'efghijkldade'

    print(sort_numbers(''))
    assert sort_numbers('') == ''

    print(sort_numbers(' Ten Nine Eight'))
    assert sort_numbers(' Ten Nine Eight') == 'ten nine eight'

    print(sort_numbers('FIVE'))
    assert sort_numbers('FIVE') == 'five'
```