```python
def modp(n, p):
    return (1 << n) % p
```

This function takes two inputs, `n` and `p`, and returns the result of `1 << n` modulo `p`. 

It's a good idea to ensure this solution behaves correctly on the edge cases tested in the problem statement. These test cases could be incorporated into a self-contained script to fully solve the problem as you requested:
```python
import unittest

def modp(n, p):
    return (1 << n) % p

class TestModp(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()
```

This script includes the `modp` function and a unittest class `TestModp` with test cases that assert the function's behavior matches the problem statement. When executed, this script will run the tests and print out the results, which should all say `OK`. 

Let me know if you have any more questions!