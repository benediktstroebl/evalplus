```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    : Count-overlapping cases. Returns the number of times of occurrence of substring in string.
    :string, substring -> Counter()
    : Counter object
    <start,end> --> Counter.each/Indexer
    count
    : Count occurrences
    """
    return Counter(string.find(substring, start=1, end=len(substring))).  # this line is a heuristic to improve performance, not required
    ```