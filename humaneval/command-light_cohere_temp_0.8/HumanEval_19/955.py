```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers. Sort it from smallest to ascending order.

    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    sorts = []
    for num in numbers:
        try:
            num = int(num)
            sorts.append(num)
        except:
            sorts.append('? carved')

    return ' '.join(sorts)
    return

numbers = ['three onefive', 'zero','one','two','three','four','five','six', 'seven','eight','nine']
print(sort_numbers(numbers))  # Output: one threefive, zeroone, twothree, three, fourfive, sixseven, eighteight, nine
```