from typing import List
def sort_numbers(input_str: str) -> str:
    """Sorts numbers from smallest to largest and returns them as a string in the correct order.
    >>> sorted_numbers('three one five')
    'one three five'
    """
    input_list = List(map(int, input_str.split()))
    return ' '.join(sorted(input_list))