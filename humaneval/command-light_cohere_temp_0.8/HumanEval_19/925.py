```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are random. Return the string with numbers sorted from smallest to largest"""
    return numbers.split(" "). spaces)[::-2]. number + str.len()]  .join real numbers from

numbers = ['three onefive', 'two seven eight', 'six four nine', 'eight six three']
test_cases = [
    "zero one two three four five six seven eight nine"
    , "onesee fivesix seven eight"
    , "onetwothree four five six seven eight nine"
    , "threesixes seven eight nine"
]

for case in test_cases:
    actual = sort_numbers(case)
    assert actual == case
    print("Passed test:", actual)
```