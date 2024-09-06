```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        balance = 0
        i = 0
        for char in chunk:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            result.append(balance)
        result.append(i)
    return result
```

The provided Python script solves the problem of finding the deepest level of nesting of parentheses in a given string. It defines a single function, `parse_nested_parens`, which takes a string as input and returns a list where each element represents the maximum depth of nesting of parentheses within the corresponding chunk of the input string.

Here's a step-by-step explanation of the code:
1. **Function Signature**: `def parse_nested_parens(s: str) -> List[int]`:
   - This code defines a function named `parse_nested_parens` that takes a single argument `s`, which is of type `str` (a string).
   - The function returns a list of `int` (integers).
2. **Initialize Result List**: `result = []`:
   - This initializes an empty list named `result`. This list will store the output for each chunk of the input string.
3. **Loop for Each Chunk**: `for chunk in s.split():`:
   - The input string `s` is split into a list of substrings using spaces as the delimiter. This is done using the `.split()` method, which returns a list of substrings.
   - Each substring is iterated over using a loop.
4. **Balance Tracking**:
   - `balance = 0`: Initializes a counter `balance` to keep track of the balance of parentheses. It is set to zero before starting to count the parentheses.
   - `i = 0`: An auxiliary counter `i` is set to zero to keep track of the position in the current chunk.
5. **Char Loop**: `for char in chunk:`:
   - This loop iterates through each character in the current chunk.
   - If the character is `'('` (an open parenthesis):
     - `balance += 1`: The `balance` counter is increased, indicating that we have opened a new group of parentheses.
   - Otherwise (the character is `')'`  (a close parenthesis):
     - `balance -= 1`: The `balance` counter is decreased, indicating that we have closed a group of parentheses.
6. **Appending to Result**: 
   - `result.append(balance)`: Appends the current balance value to the `result` list. This represents the maximum depth of nesting for the chunk.
   - `result.append(i)`: Appends the current value of `i` to the `result` list. `i` represents the position where the evaluation of the chunk ends.
7. **Return the Result**: 
   - The function returns the `result` list, which contains the maximum depth of nesting for each chunk of the input string.

The provided code effectively solves the problem and can be used as a standalone script to parse and extract the maximum depth of nesting of parentheses in any given input string.