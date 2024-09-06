Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz_sequence = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz_sequence.append(num)
    return odd_collatz_sequence

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_basic(self):
            """
            Test the get_odd_collatz function for basic cases.
            """
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])
            self.assertEqual(get_odd_collatz(14), [1, 7, 11, 14])

        def test_get_odd_collatz_edge(self):
            """
            Test the get_odd_collatz function for edge cases.
            """
            self.assertEqual(get_odd_collatz(0), [])
            self.assertEqual(get_odd_collatz(2), [1, 2])
            self.assertEqual(get_odd_collatz(3), [1, 3])
            self.assertEqual(get_odd_collatz(100), [1, 5, 21, 85, 141, 197, 293, 389, 461, 593, 661, 751, 831, 921, 1019, 1105, 1193, 1289, 1369, 1459, 1529, 1609, 1699, 1797, 1919, 1997, 2017, 2117, 2195, 2293, 2391, 2489, 2569, 2657, 2737, 2817, 2877, 2947, 3017, 3077, 3137, 3207, 3277, 3337, 3397, 3457, 3517, 3577, 3637, 3697, 3747, 3817, 3877, 3947, 4017, 4077, 4137, 4207, 4277, 4337, 4397, 4457, 4517, 4577, 4637, 4697, 4747, 4817, 4877, 4947, 5017, 5077, 5137, 5207, 5277, 5337, 5397, 5457, 5517, 5577, 5637, 5697, 5747, 5817, 5877, 5947, 6017, 6077, 6137, 6207, 6277, 6337, 6397, 6457, 6517, 6577, 6637, 6697, 6747, 6817, 6877, 6947, 7017, 7077, 7137, 7207, 7277, 7337, 7397, 7457, 7517, 7577, 7637, 7697, 7747, 7817, 7877, 7947, 8017, 8077, 8137, 8207, 8277, 8337, 8397, 8457, 8517, 8577, 8637, 8697, 8747, 8817, 8877, 8947, 9017, 9077, 9137, 9207, 9277, 9337, 9397, 9457, 9517, 9577, 9637, 9697, 9747, 9817, 9877, 9947
if __name__ == '__main