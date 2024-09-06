Here is a self-contained Python script that solves the problem of scaling Markdown code blocks:

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [0] + numbers
    for x in numbers:
        numbers.append(x) * x/2)
    return numbers

def test_rescale_to_unit(test_cases: List[List[str]]) -> List[bool]:
    """ Test the rescale_to_unit function with a list of test cases
    >>> test_cases = [[
        
    "** Hello**", 
    "## World",
    "### Programming", 
    "!# structure, 
    "!is ** Good.", 
    "!is ** me,!"**
    "!is ** table."], 
    [5,09, 
    "."""]
    for test_case in test_cases:
        for case in test_case:
            if not rescale_to_unit(case.split('\n) :
                return False
        return True
    return [True]

test_rescale_to_unit([['Hello', 'World', 'Programming', 'Good', 'Table'])

This function test_rescale_to_unit accepts a list of strings, which are split into lists of substrings using the split() method. The strings in the lists are then passed to the rescale_to_unit function. The resulting numbers are appended to a new list, with values multiplied by 2 and the smallest number becoming 0. The test_rescale_to_unit function accepts a list of test cases and returns a list of True values if all test cases pass, and False otherwise.

The test_rescale_to_unit function is a simple and straightforward way to test the rescale_to_unit function. It is easy to write and read, and it can be used to test the function with different input values. This function can be used to verify that the rescale_to_unit function is working correctly.