```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the given substring can be found in the original string.
    """
   

    substring = substring.lower()
    how many string = string.lower()
    how many substring and string.

    count = 0
    str.count(substring)
    str.find(substring, string)
    count += 1
    return count

# Test case 1
test_1 = how_many_times('aaa', 'aa')
assert test_1 == 3

# Test case 2
test_2 = how_many_times('iii', 'i')
assert test_2 == 2

# Test case 3
test_3 = how_many_times('a', 'a')
assert test_3 == 0

```