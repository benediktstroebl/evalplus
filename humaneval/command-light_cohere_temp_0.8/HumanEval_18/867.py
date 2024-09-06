```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)
 
# Test
test_case1 = "aaaaaa"
test_case2 = "abbc"
test_case3 = "aabb"
test_case4 = " debating a    b  students"
test_case5 = "This is a debating   students."
test_case6 = "a"

assert how_many_times(test_case1, "a") == 6
assert how_many_times(test_case2, "a") == 3
assert how_many_times(test_case3, "aa") == 2
assert how_many_times(test_case4, "a") == 0
assert how_many_times(test_case5, "debating a") == 3
assert how_many_times(test_case6, "a") == 1
```