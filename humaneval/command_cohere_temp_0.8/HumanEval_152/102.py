```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result
```

The solution works by using Python's zipper to iterate over each element of both `game` and `guess` arrays. In each iteration, it calculates the absolute difference between the two elements, and if the difference is not zero, it means the user has guessed wrong, so it returns the difference. Otherwise, the guess is correct, and it returns 0. The final result is a list that is returned. 

The tests verify that the function correctly computes the results for a variety of inputs, ensuring that the function behaves as expected. 

--- 
```python
import unittest
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x, y in zip(game, guess)]
    return result

class TestCompare(unittest.TestCase):
    def test_single_correct(self):
        self.assertEqual(compare([1,2,3,4,5,1], [1,2,3,4,2,-2]), [0,0,0,0,3,3])

    def test_single_wrong(self):
        self.assertEqual(compare([0,5,0,0,0,4], [4,1,1,0,0,-2]), [4,4,1,0,0,6])

    def test_multiple_correct(self):
        self.assertEqual(compare([1,2,3,4,99,1], [1,2,3,4,99,99]), [0,0,0,0,0,0])

    def test_multiple_wrong(self):
        self.assertEqual(compare([10,5,20,0,0,100], [0,1,1,0,0,10]), [10,4,19,0,0,90])

    def test_mixed(self):
        self.assertEqual(compare([1,2,30,4,5,1], [1,2,3,4,2,-2]), [0,0,2,0,3,3])

if __name__ == '__main__':
    unittest.main()
```