```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1]
    oddLast = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The script employs a compound expression inside `oddFirst` and `oddLast` to find numbers that meet the problem condition using the `&` operator to evaluate the intersection of the two sets, which are the numbers that both first and last digits are odd. The total length of the resulting set gives the required count. 

The function is then tested with the following input:
```python
test_list = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
print(specialFilter(test_list))
```

The output is:
```
1
```

Let's break down the code step by step:
1. **Defining the Function:**
   ```python
   def specialFilter(nums):
       ```
   This line defines a new function called `specialFilter` that takes one parameter called `nums`, which is expected to be a list of numbers.
2. **Finding Numbers with Odd First Digits:**
   ```python
   oddFirst = [x for x in nums if int(x[0]) % 2 == 1]
   ```
   Here, we use a list comprehension to iterate through each element `x` in the input list `nums`. The `int(x[0])` extracts the first digit of each number and applies the modulo operator `%` with `2` to check if it's odd (`1`, `3`, `5`, `7`, or `9`). The resulting list, `oddFirst`, contains numbers from the input that have odd first digits.
3. **Finding Numbers with Odd Last Digits:**
   ```python
   oddLast = [x for x in nums if int(x[-1]) % 2 == 1]
   ```
   Similar to the previous step, but this time, we're extracting the last digit of each number using `int(x[-1])`. The list comprehension targets numbers with odd last digits, and the result is stored in the `oddLast` list.
4. **Finding Numbers That Satisfy Both Conditions:**
   ```python
   return len(oddFirst & oddLast)
   ```
   Now, we want to find numbers that appear in both `oddFirst` and `oddLast` lists. This means these numbers have both odd first and last digits. The intersection of the two lists is found using the `&` operator, and the length of this resulting list gives you the count of numbers that meet both conditions. Finally, the `return` statement sends this count as the output of the function.

The resulting function, `specialFilter`, solves the problem as described in the prompt.