Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. Then it returns the length of this set which gives the number of distinct characters. 

The function can be tested as follows:
```python
import unittest
def test_function():
    testString1 = 'xyzXYZ'
    testString2 = 'Jerry'
    testString3 = 'TestString'
    correctAnswer1 = 3
   correctAnswer2 = 4
    correctAnswer3 = 8
    testCase1 = unittest.TestCase()
    testCase1.assertEqual(count_distinct_characters(testString1),correctAnswer1)
    testCase2 = unittest.TestCase()
    testCase2.assertEqual(count_distinct_characters(testString2),correctAnswer2)
    testCase3 = unittest.TestCase()
    testCase3.assertEqual(count_distinct_characters(testString3),correctAnswer3)
    unittest.main()
test_function()
``` 
This will correctly test the function.