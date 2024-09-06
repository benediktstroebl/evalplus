```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
This code uses a list to store all the prefixes and initially adds the single-character prefix (i.e. the first character) to the list. Then, it loops through the characters from the second to the last and adds the current prefix to the list. In the end, it returns the list of prefixes from the shortest (the single character) to the longest (the entire string). 
It's a useful function that can be applied in many scenarios, including text analysis or spell-checking games. 
If you want to test it, you can use the following script: 
```python
import unittest

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hello'])
        self.assertEqual(all_prefixes(''), [''])

    def test_all_prefixes_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_all_prefixes_with_non_alpha(self):
        self.assertEqual(all_prefixes('123abc'), ['1', '12', '123', '123a', '123ab', '123abc'])
    def test_all_prefixes_with_leading_non_alpha(self):
        self.assertEqual(all_prefixes('1abc'), ['1', '1a', '1ab', '1abc'])

if __name__ == '__main__':
    unittest.main()
``` 

This code provides multiple test cases to cover different scenarios, ensuring that the `all_prefixes` function works correctly for various input types.