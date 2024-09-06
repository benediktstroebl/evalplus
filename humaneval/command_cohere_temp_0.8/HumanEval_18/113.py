Here's a Python script that contains a function called `how_many_times` that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            count += 1
    return count
```
The function takes two arguments, the `string` and the `substring`, and counts the number of times the `substring` occurs in the `string`, including overlapping occurrences. The code uses a for loop to iterate over each possible start position of the substring and then checks if the substrings match. The count variable is incremented if they do match. Finally, the function returns the count.

Here is a test suite to ensure it works correctly:
```python
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'aa') == 1
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aaaa') == 1
    assert how_many_times('abcd', 'cd') == 2
```
The test suite covers various scenarios to ensure the function behaves correctly. You can use these test cases to verify that the function works as expected on different inputs.  This way, you can have more confidence in the solution's correctness.  You can run these tests using the `python -m unittest test_how_many_times` command.  This will run the tests and display the results, indicating whether the function is operating as expected.  If all the tests pass, it will indicate in the output. If any of the tests fail, it will show which test(s) failed and what the problem seemed to be.  This helps in debugging and ensuring the correctness of the solution.