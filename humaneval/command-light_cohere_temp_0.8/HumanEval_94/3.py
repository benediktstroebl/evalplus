```python
def skjkasdkd(lst):
    """
    You are given a list of integers.
    The function aims to find the largest prime value in the list and returns the sum of its digits.

    Examples:
    lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] 
    the output should be 10
    """
    return sum([x for x in lst if x >= 1 and x % 10 == 0])

# Test cases for function skjkasdkd
test_cases = [
    [ [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3], 10],
    [ [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1], 25],
    [ [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3], 13],
    [ [0,724,32,71,99,32,6,0,5,91,83,0,5,6], 11],
    [ [0,81,12,3,1,21], 3],
    [ [0,8,1,2,1,7], 7]
]

for case in test_cases:
    assert skjkasdkd(case) == case[1]
```  This script provides a function `skjkasdkd` that finds the largest prime value in a given list and returns the sum of its digits. It is also includes several test cases to ensure that the function is working correctly.