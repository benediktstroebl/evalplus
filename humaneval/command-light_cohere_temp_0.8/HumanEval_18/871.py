```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test suite
test_suite = unittest.TestCase('')
def test_many_times():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abc', 'a') == 2
    assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('abcde', 'ab') == 2

if __name__ == "__main__":
    unittest.run_unittest(test_suite)
```
This code defines a function `how_many_times` that takes a string and a substring as input and returns the count of occurrences of the substring in the original string. 

It uses a loop to iterate through each character in the string and counts the occurrences of the substring. 

The `test_many_times` function is a test suite that verifies the correctness of the `how_many_times` function. It uses the `unittest.TestCase` library to define a test case with multiple strings and substring.

Finally, the `if __name__ == "__main__":` statement ensures that the test suite is executed only when the script is run directly.