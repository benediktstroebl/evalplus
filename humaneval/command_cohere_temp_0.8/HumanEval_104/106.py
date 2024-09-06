```python
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in x]
    return sorted(odd_digits)
``` 

The function `unique_digits` checks all the digits in the integer n, and builds a new integer `odd_digits` with the odd digits of n. Then it removes the integer from the list `x`. This process is done in a recursive manner, and eventually, all the even-digit integers will be removed from the list `x`. The lambda function `(x for x in str(n) if x.isdigit() and x % 2 != 0)` creates a generator expression that iterates over each digit in the string representation of the number n, checking if each digit is odd. 

The following is a test case that can be used to verify the functionality of the function:
```python
test = [(15,33,1422,1,[1,15,33]), 
        (152,323,1422,10,[]),
        (22, 444, 1238, 9900, [22, 444, 1238, 9900])]
for case in test:
    assert unique_digits(case[0:5]) == case[5]
``` 
This test case contains multiple lists of integers, and for each list, it checks if the output of the function is correct. 

The expected output for the test cases is:
```bash
[1, 15, 33]
[]
[22, 444, 1238, 9900]
``` 
The first test case returns a list of 3 odd digits [1, 15, 33], the second test case returns an empty list since all the elements have even digits, and the third test case returns all the elements with odd digits.