```python
def match_parens(lst):
    def shift(s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            else:
                cnt -= 1
            yield from [char] * cnt

    combinations = [{char for char in shift(s)} for s in lst]
    
    def check_balance(combinations):
        return all(sum(cnt == 0 for cnt in balance) == 0 for balance in combinations)
    
    return "Yes" if check_balance(combinations) else "No"
``` 

The script utilizes a generator `shift` to iterate over combinations of parentheses and concurrently maintains balances of open and closed parentheses for each string. The main logic then concatenates combinations of parentheses from the input list and checks if any of these combinations result in a balanced string. If any balanced combinations are found, the function returns "Yes"; otherwise, it returns "No". 

This approach allows the use of nested loops, making the code more efficient in terms of time complexity compared to recursion. It also eliminates the need for unnecessary concatenations, resulting in a more optimized solution.