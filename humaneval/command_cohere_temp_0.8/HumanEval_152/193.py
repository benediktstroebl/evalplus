```python
def compare(game, guess):
    return [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
```
This function takes two equal-length arrays, `game` and `guess`, where each element corresponds to the actual result of a match and the predicted result respectively. It returns an array of the same length where each element is the absolute difference between the guess and the score if they didn't guess correctly, and 0 if the guess was correct. The function is encapsulated in a self-contained Python script, ready to be executed independently. 

Here is an example of how to use the script for the provided test cases:
```python
import unittest
from compare import compare

class TestCompare(unittest.TestCase):
    def test_example1(self):
        game = [1,2,3,4,5,1]
        guess = [1,2,3,4,2,-2]
        self.assertEqual(compare(game, guess), [0,0,0,0,3,3])

    def test_example2(self):
        game = [0,5,0,0,0,4]
        guess = [4,1,1,0,0,-2]
        self.assertEqual(compare(game, guess), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()
```

The script is also compatible with Python 3.8 and higher versions. You can execute the script by running `python script.py` and it will automatically run the test cases and print the results.  This solution utilizes Python's powerful array manipulation capabilities and element-wise operations, demonstrated through the use of the `zip()` function to iterate through pairs of corresponding elements in the 'game' and 'guess' arrays, calculating the absolute differences, and returning an array of those differences. 

Make sure you are running Python 3.8 or higher to ensure that the `unittest` module is available, which is utilized for the test cases included in the script.  This way, you can validate your solution and ensure it passes the given tests, proving its functionality and correctness.  If the `unittest` module is not available, the script will raise a `NameError`.  In that case, you can manually add the `compare` function to a Python file and execute that file separately to test the function.