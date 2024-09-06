```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test_cases = [ ("", "a"), ("aaa", "aaaa"), ("""aaaaa""aa") ]
for case in test_cases:
    assert how_many_times(case, "a") == 3, f"incorrect for {case} (expected 3, got {how_many_times(case, 'a')})"
``` 
This code defines a function, `how_many_times`, that calculates the frequency of a given substring within a given string. It utilizes a recent iteration method, which counts the number of instances of the substring found in the input string.