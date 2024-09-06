```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            if i in seen and l.count(i) > 1:
                return True
            seen.add(i)
        else:
            if -i in seen and l.count(-i) > 1:
                return True
            seen.add(-i)
    return False
```

This code solves the problem by iterating through the list `l` and checking if any of its elements have more than one occurrence. If so, it checks whether their positive or negative counterparts also occur in the list, and if they do, the function returns True. Otherwise, it returns False. 

This solution follows the specification you provided, and should work correctly for the test cases mentioned. You can embed it within a markdown code block surrounded by triple backticks, `'```'` to include it in a Markdown document.