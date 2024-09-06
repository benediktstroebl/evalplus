```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through the list, tracking integers it has seen.

For positive integers, it checks if the integer has previously been seen and if there are multiple occurrences of this integer in the list.

For negative integers, it checks if the integer's negative has previously been seen and if there are multiple occurrences of this negative integer in the list.

It returns True if any of these conditions are met, indicating the presence of two elements whose sum equals zero, and False otherwise.

This approach ensures efficiency and adheres strictly to the problem statement.

The unit tests provided for this function are rudimentary and may benefit from additional scenarios covering edge cases and different list compositions.

Feel free to customize the tests further to suit your needs. 
If you prefer a different solution or have additional questions, let me know! Feel free to ask for further clarifications or provide any feedback you have on how I can better assist you.