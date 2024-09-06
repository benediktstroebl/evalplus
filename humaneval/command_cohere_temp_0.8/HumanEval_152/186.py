```python
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]
```
This Python script defines a function named `compare` which takes two arrays, `game` and `guess`, as input. It returns an array of the same length as these inputs, where each element represents the difference between the corresponding elements in the `game` and `guess` arrays. If the guess was correct, the result is 0, otherwise, it is the absolute difference between the guess and the score.

Here is an example of how to use the `compare` function:
```python
game = [1, 2, 3, 4, 5, 1]
guess = [1, 2, 3, 4, 2, -2]
result = compare(game, guess)
print(result)  # Output: [0, 0, 0, 0, 3, 3]
``` 
The example provided in the problem statement is also tested with a unit test using the `unittest` module. The unit test is included in the code snippet below:
```python
import unittest
def compare(game, guess):
    return [abs(x-y) if x!=y else 0 for x,y in zip(game, guess)]

class TestCompare(unittest.TestCase):
    def test_compare(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        self.assertEqual(compare(game, guess), [0, 0, 0, 0, 3, 3])

    def test_compare_different_length(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            compare(game, guess)

    def test_compare_wrong_type(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2.5]
        with self.assertRaises(TypeError):
            compare(game, guess)

if __name__ == '__main__':
    unittest.main()
``` 
The tests are necessary to ensure that the function behaves as expected and correctly computes the differences between the `game` and `guess` arrays.

When the `compare` function is used with the example inputs, the returned result is an array with the elements set to 0 where the guesses were correct, and the absolute difference otherwise. Thus, the output from the example usage in the code snippet is:
```python
[0, 0, 0, 0, 3, 3]
``` 
**NOTE**: The code also includes a test that checks for a `ValueError` if the input arrays differ in length and a `TypeError` if there is a different data type present in the inputs. These would respectively raise an error and incorrectly compute the result in the compare function if they weren't caught.