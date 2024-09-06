```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string input `s` and returns the length of that string. The function utilizes the `len()` function, which is a built-in Python function specifically designed to determine the length of a given sequence, including strings. This code ensures the calculation of the string length is performed accurately and efficiently.

This function is self-contained, requiring no external dependencies or additional functionality. It specifically addresses the problem of calculating the length of a given string and provides a straightforward solution for that requirement. 

To verify the correctness of the `strlen` function, you can write tests that assert the function's behavior against specific inputs. For example, you can use Python's `unittest` module to create a test case for each example provided in the problem statement. 

Here's an example of how you can test this function:
```python
import unittest

def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen("abc"), 3)

if __name__ == "__main__":
    unittest.main()
```

In this example, `unittest` is employed to conduct testing within a specific test class named `TestStringLength`. Within this class, there are two distinct test methods, namely `test_empty_string` and `test_non_empty_string`. In the first method, the input is an empty string, and the assertion checks if the `strlen` function returns 0, which is the expected behavior. Meanwhile, the second method uses a non-empty string as input and verifies that the function's result is 3, which corresponds to the length of the given string. 

By executing this code, you can validate the correctness of the `strlen` function against diverse test cases, offering confidence in its behavior and ensuring its efficacy in solving the presented problem.