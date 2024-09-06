Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

The function works by using the `reversed` function to iterate through the input string from the end to the beginning. By doing this, the function can identify the outermost parentheses first and avoid nesting problems; using `reversed` is not strictly necessary, but it makes the logic more straightforward. It uses the tuple `(*brace_stack)` to keep track of the parentheses encountered as it iterates through the string. The `brace_stack` is initialized with `('(', ')', 0)` to represent the opening parenthesis of the outermost group, the closing parenthesis, and the current depth of nesting (initially zero).

The function repeatedly removes each parenthesis from the string and pushes it to a list if the closing parenthesis is encountered at the current nesting depth. If a closing parenthesis is encountered that doesn't match the current nesting depth, it is ignored and processed as an unrelated closing parenthesis. Also, to handle weird strings with unbalanced parentheses, we catch the `IndexError` that happens when there are less opening parentheses than expected.

Note that the parameter `brace_special` is a tuple of strings, where each string contains a set of parentheses. This is used to determine whether an opening or closing parenthesis is part of the current group being processed or the next group. 

Here's the code:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    brace_stack = ('(', ')', 0)
    paren_list = []
    brace_special = ('(', ')', '}')

    # using iter(reversed(input_string)) to optimize
    for char in iter(reversed(paren_string)):
        # If the character is an opening brace and we are at the right depth, add it to the stack
        if char == brace_stack[0] and brace_stack[2] == 0:
            brace_stack = tuple(brace_stack) + (char, )
            brace_stack[2] += 1
        # If the character is a closing brace and we are at the right depth, add it to the list and decrement the depth
        elif char == brace_stack[1] and brace_stack[2] > 0:
            brace_stack = tuple(brace_stack)[:-1]
            brace_stack[2] -= 1
        # If the character is an opening brace for a new group and we are at the right depth, add it to the list and increment the depth
        elif (char == brace_stack[0] and brace_stack[2] == 0 and
              not (char in brace_special and brace_stack[1] in brace_special[1:])) or
              char == brace_stack[1] and brace_stack[2] > 0:
            paren_list.append(char)
            brace_stack = tuple(brace_stack) + (char, 0)
        # If we encounter a closing brace that doesn't match the current depth, it belongs to a nested group
        elif char == brace_stack[1] and brace_stack[2] == 0:
            brace_stack = tuple(brace_stack) + (char, 0)
        # In case of unbalanced or weird input, catch the error and add the incorrect closing brace to the stack
        except IndexError:
            brace_stack = tuple(brace_stack) + (char, 0)

    # Add the last group
    if brace_