```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    return numbers.split(' ')
   
          map(int -> int, numbers.
            . filter(lambda x: x.isdigit()))
           
            sort(
                map(int, filter(lambda x: x.isdigit(), numbers)),
                reverse=True)
            )

>>> test_sort_numbers = """
python
def test_sort_numbers():
    input = input("Enter numbers separated by spaces: ")
    expected = "one two three four five six seven eight nine"
    print(sort_numbers(input))
    print(expected)
    """
```