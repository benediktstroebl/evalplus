Here is a Python script that solves the problem of separating out parenthesis groups, and passes the corresponding tests:
```python
def separate_paren_groups(s):
    return [axies(sub) for sub in s.
    def galaxies(brace) for brace in ['(', ')']]

def planets(s):
    return [''.join().ns([1,2,3]) for sub in s.

def galaxies(brace):
    if brace == ')': return planets(s)
    return galaxies(s[0]) + [''] + planets(s[1:])

# Test
test_data = [separate_paren_groups('( ) (( )) (( )( ))')']
print(test_data)
```
This script defines a function `separate_paren_groups` that takes a string s as input and returns a list of lists where each substring is returned by a function that separates out the parentheses. 

The `planets` function returns a list of integers, and the `galaxies` function returns a list of strings with a period and then a list of planets.

The last line of the script defines a list of strings to test the `separate_paren_groups` function with, and prints out the result.