```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Unit tests
test_how_many_times = TestCases()
test_how_many_times.assertEqual( ("a", 1))
test_how_many_times.assertEqual("aaa", "aa")
test_how_many_times.check("aaaa", "aa")
test_how_many_times.assertEqual('zzz', "zzz")
test_how_many_times.has("bees", "ess")
```
The above code defines a function how_many_times that returns the number of times a given substring can be found in the original string. The function uses the iterating over the characters in the substring and checking if each character is present in the string.