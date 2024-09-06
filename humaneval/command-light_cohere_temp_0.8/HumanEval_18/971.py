```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test suite
def test():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3

if __name__ == "__main__":
    test()
```  The function ```how_many_times``` takes a string and a substring as input and returns the number of occurrences of the substring in the original string. The function uses a loop to iterate through the string and count the occurrences of the substring.