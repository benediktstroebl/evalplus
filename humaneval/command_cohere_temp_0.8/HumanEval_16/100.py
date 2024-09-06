Here's a Python script that contains a function to solve the problem you've described:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the provided string, ignoring case, and then returns the set's length to provide the number of distinct characters. 

To apply this solution, you can directly use the function as shown in the docstring:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
```
Ensuring that it produces the desired outcome.  This approach eliminates the need for a counter variable, and uses the built-in functionalities of Python to efficiently solve the problem.