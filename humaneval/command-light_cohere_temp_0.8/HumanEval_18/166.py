```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.
    """ 
    return sum(1 for i, j in string. strings.find(substring, 
        if i == j) else 0
    )

# Example function test
def test():
    assert how_many_times('aaa', 'aa') == 3

# Driver code
if __name__ == "__main__":
    test()
```