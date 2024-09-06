```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group.split(' '))))
                        for group in s.split(' '))
            for _ in range(len(s))]
```

The code uses a generator expression nested in a list comprehension to parse and accumulate the results.

To achieve this, it employs the following steps:
1. The function takes a string as input, which is a concatenation of several strings, each representing a group of parentheses, separated by spaces. 
2. It uses the split(' ') method to separate each group of parentheses. 
3. The map(int, group.split(' ')) converts each group into a list of numbers representing the depths of parentheses, where '(' is 1 and ')' is 0. 
4. The sum function adds up all the depths in a group to get the total depth. 
5. The reversed function allows to find the maximum depth by passing the total depth through the maximum function. 
6. The outer list comprehension goes over each group and calculates the maximum depth of nesting. In the end, the list of maximum depths for each group is returned. 
The function can be tested as follows:
```python
import unittest

def test_parse_nested_parens():
    tester = unittest.TestCase()
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    tester.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])
```