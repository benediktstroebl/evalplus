Here is a self-contained Python script that includes a function that calculates the frequency of a substring within a given string:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    return len(re.search(subpeir(substring, string))

def test_function():
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abc", "a") == 3
    assert how_many_times("sdsf", "s") == 0
    assert how_many_times("", " ")) == 0

if __name__ == "__main__":
    test_function()
```
The function uses the `re.search` function from the particular substring in the given string, and returns the count of the occurrences. If the substring is empty, the function returns 0.