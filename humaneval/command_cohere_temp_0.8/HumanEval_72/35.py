```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function will return True if the object will fly, and False otherwise. The condition len(q) == 1 or q == q[::-1] checks if the list q is single-elemented or is a palindrome. The condition sum(q) <= w checks if the sum of the elements of q is less than or equal to the maximum possible weight w. 

### Here is the solution with the corresponding tests:
```python
import unittest

def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w

class TestWillItFly(unittest.TestCase):
    def test_example1(self):
        q = [1, 2]
        w = 5
        self.assertFalse(will_it_fly(q, w))

    def test_example2(self):
        q = [3, 2, 3]
        w = 1
        self.assertFalse(will_it_fly(q, w))

    def test_example3(self):
        q = [3, 2, 3]
        w = 9
        self.assertTrue(will_it_fly(q, w))

    def test_example4(self):
        q = [3]
        w = 5
        self.assertTrue(will_it_fly(q, w))

    def test_false_case1(self):
        q = [1, 2, 3]
        w = 9
        self.assertFalse(will_it_fly(q, w))

    def test_false_case2(self):
        q = [1, 2, 3, 4]
        w = 6
        self.assertFalse(will_it_fly(q, w))

    def test_false_case3(self):
        q = [1, 2, 3, 4, 5]
        w = 10
        self.assertFalse(will_it_fly(q, w))

    def test_true_case1(self):
        q = [2, 3, 3]
        w = 7
        self.assertTrue(will_it_fly(q, w))

    def test_true_case2(self):
        q = [1, 2, 3, 4, 5]
        w = 12
        self.assertTrue(will_it_fly(q, w))

if __name__ == '__main__':
    unittest.main()
``` 

In the test suite are included test cases that cover edge cases and different scenarios, to ensure the proper functioning of our function. 

To run the test suite save the code into a **.py** file and run the command **python <file_name>.py** in your terminal. 

You can also run the individual test cases by uncommenting the desired test case in the **if __name__ == '__main__':** block. 

**NOTE**: Replace <file_name>.py with the actual name of your file.