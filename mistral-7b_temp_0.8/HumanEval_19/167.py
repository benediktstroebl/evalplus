from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    assert 'zero' in numbers
    assert 'nine' in numbers
    assert 'one' in numbers
    assert 'two' in numbers
    assert 'three' in numbers
    assert 'four' in numbers
    assert 'five' in numbers
    assert 'six' in numbers
    assert 'seven' in numbers
    assert 'eight' in numbers

    return ''.join(sorted(numbers.split()))

