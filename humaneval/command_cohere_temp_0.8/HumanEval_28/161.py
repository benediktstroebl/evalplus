```python
# Retrieve the definition of the function to be solved
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

# Implement the solution
def solve_problem():
    def concatenate(strings: List[str]) -> str:
        result = []
        for string in strings:
            if string == '':
                continue
            else:
                result.append(string)
        return ''.join(result)
    
    return concatenate

# Unit tests
def test_empty_list():
    assert solve_problem()([], '') == ''

def test_single_string():
    assert solve_problem()(['a'], 'a') == 'a'

def test_multiple_strings():
    assert solve_problem()(['a', 'bc', 'def'], 'abcdef') == 'abcdef'

test_empty_list()
test_single_string()
test_multiple_strings()
``` 
This code provides a solution to the problem, and also incorporates three unit tests to validate its correctness against different cases. It operates by appending the strings from the list to the result list, excluding any empty strings. Subsequently, it joins the elements of the result list to produce the final output.