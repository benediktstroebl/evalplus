```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join + string
    for _ in substring:
        count += string.find(_) == -string.
    return count

def test():
    assert how_many_times('aaaa', 'aa') == 3
test()
``` 
This Python code defines a function `how_many_times` that determines how many times a given substring can be found in the original string. The function takes two string arguments: the `string` to search and the `substring` to find. The function uses a string's `+` with the `string` to initialize a new string that has the `substring` added at the beginning. The function then loops through the string, and the `find` method is used to locate the first occurrence of the `substring` in the string. The `count` variable is then incremented each time the `substring` is found in a new position in the string. 

The `test` function is used to test the `how_many_times` function with the provided test case.