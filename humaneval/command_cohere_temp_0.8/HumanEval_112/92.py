```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The problem is solved by using two nested lists comprehensions, the first comprehension deletes all the characters in s that are present in c, resulting in a new list of characters that are not in c. The second comprehension joins the list of remaining characters into a string, which is the result of the deletion. The function returns a tuple containing the deleted string and a boolean that is True if the string is a palindrome and False otherwise. 

This solution works correctly for the examples provided in the prompt and should pass all related tests. 
If you want to test this function, you can create a unittest module or use the built-in `unittest` module in Python. You can add your tests to the `unittest` module. Here's an example of how you can use the `unittest` to create a test:
```python
import unittest

def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]

class TestReverseDelete(unittest.TestCase):
    def test_abcde_ae(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_abcdef_b(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_abcdedcba_ab(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `unittest` module is used to create and run tests. The `TestReverseDelete` class derives from `unittest.TestCase`, and each test is defined as a method with the `self.assertEqual()` line, which checks if the output of the `reverse_delete` function is correct for a specific input. Finally, `unittest.main()` is called to find and run all tests.