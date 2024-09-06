Here's the self-contained Python function:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    def count(char):
        count = 0
        for i in string:
            if char == substring:
                count += 1
            if char == substring[0] and i < len(substring):
                count += 1
        return count
    return count(string)
```