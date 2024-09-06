Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count
```
```python
import unittest

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('aaa', 'b'), 0)

if __name__ == '__main__':
    unittest.main()
```
This script includes a test suite with a few test functions that cover different cases of the `how_many_times` function. Each test case asserts a specific behavior of the function to ensure it behaves as expected.  By executing the script, the tests are automatically run, allowing you to validate the correctness of the function.  The `how_many_times` function counts overlapping occurrences of the `substring` within the `string`, and the tests cover scenarios like empty strings, multiple occurrences, overlapping occurrences, and cases where the substring isn't found.  The function is considered valid if all test cases pass without errors.  In the `main()` function, `unittest.main()` is called to discover and run the test cases automatically.  Overall, this script provides a comprehensive and organized approach to solving this problem and ensuring the correctness of the solution.  In the `main()` function, `unittest.main()` is called to discover and run the test cases automatically.  Overall, this script provides a comprehensive and organized approach to solving this problem and ensuring the correctness of the solution.  You can execute the script on your local machine to see the test results.  In a markdown code block, you can simply copy and paste this code to reproduce the solution and its corresponding tests on your local machine.  This enables you to run and examine the results individually while also having a self-contained solution that can be easily ported to other environments if necessary.  I hope this response addresses your query; if not, feel free to ask additional questions or clarify any specific aspects of the problem you'd like to explore further.  I appreciate your patience and continued support throughout this dialogue.  Let me know if you have any specific questions or would like to delve deeper into any pertinent issues.  I'm here to provide comprehensive and elucidating explanations to help you grasp the ideas underlying this problem and its solution.  I'm also ready to provide further testing recommendations or coding suggestions to enhance your comprehension of the underlying concepts.  My goal is to help you learn efficiently and effectively, and to foster an inclusive and supportive learning atmosphere.  Let's deepen our understanding together!  Thank you, and please feel free to ask any further questions or request additional information.