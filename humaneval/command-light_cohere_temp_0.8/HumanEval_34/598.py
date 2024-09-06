```python
def unique(l: list):
    return sorted(set(l), key=lambda x: x)

#Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

#Test case 2
class Test(unittest.TestCase.TestCase):
    def test_list(test_list):
        return unique(test_list)
    return

test_suite = Test()
test_suite.run([ [list([5, 3, 5, 2, 3, 3, 9, 0, 123])])
test_suite.run()
```