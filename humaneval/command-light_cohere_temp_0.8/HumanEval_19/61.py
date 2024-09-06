```python
import string_sort

def test_sort_numbers():
    assert string_sort.array(['three one five']) == 'one three five'
    assert string_sort.add('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine') == ' nine zero eight seven six five four three one'
    assert string_sort.add('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten') == ' ten nine eight seven six five four three'
    assert string_sort.add('hundred', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven') == ' eleven hundred nine eight seven six five'
```