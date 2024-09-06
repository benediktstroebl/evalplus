```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = str.replace(substring, "", string, 1) 
    while string.find(substring) != None:
        count += 1
        string = str.replace(substring, "", string, 1)
    return count

# Test the function
def test():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcdeef', 'def') == 3
    assert how_many_times('123456', '456') == 4
```