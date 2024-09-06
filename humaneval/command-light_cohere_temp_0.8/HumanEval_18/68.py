```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within the original string, 
    accounting for case-insensitive matches and overlapping substring occurrences.
    Returns: number of positions where the substring can be found.
    """ 
    def count_positions(string, substring):
        positions = []
        i = 0
        while i < len(string):
            if string[i] == substring:
                positions.append(i)
                i += 1
            if i == len(string):
                break
        return positions

    positions = count_positions(string, substring)
    return positions.length
```