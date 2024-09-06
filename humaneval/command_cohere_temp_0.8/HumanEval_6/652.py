```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])),  # zip creates pairs, and unpacking tuple to list converts pairs into lists
            iter(filter(lambda c: c == '(', s.split()))))))) for _ in s.split()]
```

The provided solution utilizes list comprehensions and generators to efficiently parse the input string s, find all nested parentheses, 
and determine the deepest level of nesting for each group. Let's break down the code step by step:
1. **Sum of Comprehensions**: The line sum(map(lambda x: list(zip(x, x[1:])), ...) compiles a list of lists, where each inner list is a pair of matching parentheses. 
The lambda function list(zip(x, x[1:])) builds a list of tuples where the first element is the opening parenthesis and the second element is the corresponding closing parenthesis.
The sum function then aggregates these lists of pairs.
2. **Length of Each Group**: The line max(i // 2 for i in reversed(...) calculates the maximum depth of nesting for each group of parentheses. 
For each inner list of pairs, the i // 2 calculates the number of pairs of parentheses, i.e., the number of times the depth of nesting can be divided by 2 to get the actual nesting level. Reversing the list allows us to find the maximum level from the largest number of pairs.
3. **Filtering Out Empty Groups**: The iter(filter(lambda c: c == '(', s.split())) generator filters out the empty strings that are created from splitting the input string by spaces, leaving only the strings representing parentheses groups.
4. **Iterating Over Groups**: The final for _ in s.split() iterates over the filtered groups of parentheses, extracting the deepest level of nesting for each group as calculated in step 2. 

The function returns a list of these deepest nesting levels for all groups present in the input string.