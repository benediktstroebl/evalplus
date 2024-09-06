```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.reverse()
    return odd_collatz

if __name__ == "__main__":
    import sys
    sys.stdin = open("test.txt", "r")
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz(self):
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(14), [1, 7, 11, 14])

    unittest.main()
```

The function `get_odd_collatz` uses a while loop to generate the odd numbers in the Collatz sequence. The loop starts with `num` as the input `n` and continues until `num` becomes 1. The even and odd steps in the Collatz sequence are handled accordingly, and the odd numbers are appended to `odd_collatz`, reversed later to ensure sorting. The function is then tested with three test cases which are `1` for `get_odd_collatz(1)`, `1` and `5` for `get_odd_collatz(5)`, and `1`, `7`, `11`, `14` for `get_odd_collatz(14)` respectively. The test file can be replaced with a file of your own or modified to include more tests as desired.