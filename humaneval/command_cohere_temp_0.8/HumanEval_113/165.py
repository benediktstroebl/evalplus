```python
def number_of_odd(lst):
    r = []
    for id, s in enumerate(lst, start = 1):
        count = sum(1 for i in s if i % 2 != 0)
        r.append(f'the number of odd elements in the string {id} of the input.' if count == 1 else f'{count}n the string {id} of the input.')
    return r
```

The solution leverages python's built-in `enumerate` to iterate through list elements with an index as well as a string. A sum of odd digits is computed using a generator expression, and the result is formatted into a string that is appended to a result list. The `if` statement is used to determine whether an element count is 1, replacing the value with a string that is descriptive of the problem statement. Otherwise, the count is appended with an 'n' to maintain the requested string format. 

AMarkdown block can be used to present the solution within the specified code block, as follows:
```
```python
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
```
```