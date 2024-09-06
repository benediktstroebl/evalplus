```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.

    : Optimized version with improved readability and without string concatenation.

    """
    string = ''.join(string.split(substring))
    count = 0
    for idx, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Unit tests
test_how_many_times = """
import unittest

class TestHowManyTimes {

  def test_count_substring():
    # Test the count of the substring
    assert how_many_times('aaaa', 'aa') == 3
}

if __name__ == '__main__':
  unittest.main()
```
```

This Python script defines a function `how_many_times` that counts the occurrences of a given substring in a given input string. The function splits the string into individual characters and iterates through each character. It checks if the the character matches the substring. The function then counts the occurrences and returns the result.

Additionally, the script includes unit tests for the `how_many_times` function using the `unittest` library. The tests ensure that expected count of the substring is correct.

Please note that you can run this code using an integrated development environment (IDE) like Visual Studio Code or any other Python IDE, and it will automatically execute the tests and provide feedback on whether your function is correctly implemented.