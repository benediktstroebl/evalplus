Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz_seq.append(num)
    return odd_collatz_seq

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_valid(self):
            """ Test the function for a variety of inputs."""
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(14), [1, 7, 14])

        def test_get_odd_collatz_edge_cases(self):
            """ Test function for edge cases."""
            self.assertEqual(get_odd_collatz(0), [])
            self.assertEqual(get_odd_collatz(-1), [])

    unittest.main()
```

This script will run the `unittest` module that checks the `test_get_odd_collatz_valid` test case and the `test_get_odd_collatz_edge_cases` when the script is run directly. Each test case checks the validity of the output of the `get_odd_collatz` function against the expected output. 

Note that the code assumes that the `unittest` module is included in the Python environment. Would you like me to provide guidance on how to install it additionally? 

Let me know if I've understood your needs correctly, and feel free to ask any questions!