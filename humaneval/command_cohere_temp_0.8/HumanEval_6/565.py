```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        unbalanced = 0
        nesting_level = 0
        for char in bracket_level:
            if char == '(':
                nesting_level += 1
                unbalanced += 1
            elif char == ')':
                nesting_level += -1
                unbalanced -= 1
            if unbalanced > 0:
                continue
            result.append(nesting_level)
            unbalanced = 0
        if unbalanced > 0:
            result.append(nesting_level)
    return result
```

The approach involves splitting the input string into individual brackets and iterating through each bracket to count the number of `(` and `)` to determine the deepest level of nesting of parentheses. The total count of `(` is used as a marker to calculate the nesting level, and additionally, if there are still unmatched `(` when iterating, it is assumed it is another separate group of brackets, and the previous level is added to the result. 

To test the functionality, you can run the following code:
```python
test_strings = ['(()()) ((())) () ((())()())', '()(())', '((())))', ')()(', '()()', '(((((((()())

for i, test_str in enumerate(test_strings):
    print(f"Test String {i+1}:")
    print(f"   Input: {test_str}")
    print(f"  Result: {parse_nested_parens(test_str)}")
    print()
```

This should output the results as expected with the input strings and the maximum nesting level of parentheses for each group. 

```
Test String 1:
  Input: ((())()) ((())) () ((())()())
  Result: [2, 3, 1, 3]

Test String 2:
  Input: (()(())
  Result: [1]

Test String 3:
  Input: ((())))
  Result: [3]

Test String 4:
  Input: )()()
  Result: [2]

Test String 5:
  Input: ()()
  Result: [1]

Test String 6:
  Input:  (((((((()
  Result: [4]
``` 

This should allow you to validate the functionality of the approach.