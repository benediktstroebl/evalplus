Here is a Python script with a self-contained function that solves the problem you described:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    return len(re.findall(substring, string))

# Unit tests
test_many_times = []
test_many_times.append(
     """string = "aaaaaa", "aa"
      """
  assert how_many_times(string, substring) == 3
test_many_times.append(
     """string = "abcdeba", "b"
      """
  assert how_many_times(string, substring) == 3
test_many_times.append(
     substring = "abc", "x"
      """
  assert how_many_times(string, substring) == 0
test_many_times.append(
     substring = "abcd", "bc"
      """
  assert how_many_times(string, substring) == 2
test_many_times.append(
     substring = "abcdef", "ef"
      """
  assert how_many_times(string, substring) == 3

print("All tests passed")
```