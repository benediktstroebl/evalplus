Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    return odd_collatz

if __name__ == "__main__":
    import unittest

    class TestGetOddCollatz(unittest.TestCase):
        def test_get_odd_collatz_with_odd_input(self):
            """
            Test the function with an odd input
            """
            self.assertEqual(get_odd_collatz(1), [1])
            self.assertEqual(get_odd_collatz(5), [1, 5])

        def test_get_odd_collatz_with_even_input(self):
            """
            Test the function with an even input
            """
            self.assertEqual(get_odd_collatz(2), [2])
            self.assertEqual(get_odd_collatz(4), [2])

        def test_get_odd_collatz_with_large_input(self):
            """
            Test the function with a large input
            """
            self.assertEqual(
                get_odd_collatz(100),
                [
                    1,
                    5,
                    21,
                    85,
                    341,
                    1303,
                    81,
                    2721,
                    13421,
                    5461,
                    33761,
                    133301,
                    514229,
                    1771561,
                    8354641,
                    33522461,
                    110334141,
                    44244281,
                    164135861,
                    648673301,
                    2637433401,
                    9076613601,
                    3675673401,
                    13252176461,
                    5515037261,
                    1854850621,
                    7129137561,
                    2785077941,
                    9449438861,
                    3349882861,
                    13494864181,
                    5998164481,
                    2252433721,
                    7998334001,
                    29164920041,
                    9532916041,
                    3856657201,
                    1500133601,
                    630067201,
                    2125044041,
                    7209072041,
                    2460924201,
                    8321848201,
                    2642281641,
                    8643664201,
                    2684400861,
                    9296812821,
                    3487600621,
                    1579520281,
                    6393805161,
                    2124414481,
                    7178830161,
                    2489676141,
                    8395750141,
                    2697838481,
                    936030621,
                    3520770581,
                    1560525161,
                    654052041,
                    2240810161,
                    7082104181,
                    2491631441,
                    818378641,
                    269738281,
                    933285341,
                    3546150481,
                    1580631481,
                    661618641,
                    2325326281,
                    745264141,
                    2498585681,
                    839770641,
                    2791640121,
                    986104481,
                    3682636281,
                    1725460121,
                    685040141,
                    2348387881,
                    752274681,
                    2597550061,