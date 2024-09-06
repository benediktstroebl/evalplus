```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {" + str(n + 1) + "}"*n

string_sequence = {'__doc__': "string_sequence function"}

# Test case 1
test_sequence1 = [unittest.TestCase.TestCase('int', 0, 5)]
test_sequence1.setUp('string_sequence', 'testcase1')
test_sequence1.check()

# Test case 2
test_sequence2 = [unittest.TestCase.TestCase('int', 0, 4)]
test_sequence2.setUp('string_sequence', 'testcase2')
test_sequence2.check()

# Test case 3
test_sequence3 = [unittest.TestCase.TestCase('int', 1)]
test_sequence3.setUp('string_sequence', 'testcase3')
test_sequence3.check()

# Test case 4
test_sequence4 = [unittest.TestCase.TestCase('int', 4)]
test_sequence4.setUp('string_sequence', 'testcase4')
test_sequence4.test()

# Test case 5
test_sequence5 = [unittest.TestCase.TestCase('int', 5)]
test_sequence5.setUp('string_sequence', 'testcase5')
test_sequence5.test()

# Test case 6
test_sequence6 = [unittest.TestCase.TestCase('int', 0)]
test_sequence6.setA('string_sequence', 'testcase6')
test_sequence6.test()

# Test case 7
test_sequence7 = [unittest.TestCase.TestCase('int', 3)]
test_sequence7.setA('string_sequence', 'testcase7')
test_sequence7.test()

# Test case 8
test_sequence8 = [unittest.TestCase.TestCase('int', 4, 3)]
test_sequence8.setA('string_sequence', 'testcase8')
test_sequence8.test()

# Test case 9
test_sequence9 = [unittest.TestCase.TestCase('int', 2, 3)]
test_sequence9.setA('string_sequence', 'testcase9')
test_sequence9.test()

# Test case 10
test_sequence10 = [unittest.TestCase.TestCase('int', 5, 2)]
test_sequence10.setA('string_sequence', 'testcase10')
test_sequence10.test()

def main():
    unittest.main()()
```