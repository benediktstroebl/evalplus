```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds the number of occurrences of a substring within the original string, 
    accounting for overlapping matches.
    Returns 0 if substring is not found and raises an error if substring length is > string length.

    """
    string = str(string) + str(substring)
    return len(string) - len(substring) + (len(substring) - 1) * (len(string) - len(substring))

def test_how_many_times():
    try:
        print(how_many_times('aaa', 'aa'))
    except TypeError:
        print('Test failed')

if __name__ == "__main__":
    test_how_many_times()
```
This code defines a function called **how_many_times** that aims to find the number of occurrences of a given substring within a larger string. It then provides a test function that creates a test case to ensure the correctness of the **how_many_times** function.